from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from .models import Post, Comment, Category, UserProfile, CertificationLevel
from .forms import CommentForm
from django.views.decorators.http import require_POST
from django.contrib.admin.views.decorators import staff_member_required
from .forms import UserProfileForm
from django.contrib.auth.models import User


class PostList(generic.ListView):
    """
    Displays a paginated list of published blog posts.

    Attributes:
        queryset (QuerySet): The queryset of published posts ordered by creation date.
        template_name (str): The template used to render the list of posts.
        paginate_by (int): The number of posts to display per page.
    """
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blog/index.html"
    paginate_by = 6


def post_detail(request, slug):
    """
    Displays the details of a specific blog post, along with its comments.

    If the user is authenticated, their unapproved comments are shown alongside
    approved comments. If the user submits a valid comment, it is saved and marked
    as unapproved until reviewed by an admin.

    Args:
        request (HttpRequest): The HTTP request object.
        slug (str): The slug of the post to display.

    Returns:
        HttpResponse: Rendered template displaying the post details and comments.
    """
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(approved=True).order_by('-created_on')
    categories = Category.objects.annotate(post_count=Count('posts'))
    comment_count = len(comments)

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.approved = False
            comment.save()
            messages.success(
                request,
                'Your comment has been submitted and is awaiting approval.'
            )
            return redirect('post_detail', slug=slug)
    else:
        comment_form = CommentForm()

    context = {
        "post": post,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
        "categories": categories,
    }

    return render(request, "blog/post_detail.html", context)


@login_required
def comment_edit(request, slug, comment_id):
    """
    Allows a user to edit their comment on a specific blog post.

    Only the author of the comment can edit it. The edited comment is saved as
    unapproved until reviewed by an admin.

    Args:
        request (HttpRequest): The HTTP request object.
        slug (str): The slug of the post to which the comment belongs.
        comment_id (int): The ID of the comment to edit.

    Returns:
        HttpResponseRedirect: Redirects back to the post detail page.
    """
    post = get_object_or_404(Post, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        if request.method == "POST":
            comment_form = CommentForm(data=request.POST, instance=comment)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.approved = False
                comment.save()
                messages.success(request, 'Comment updated successfully!')
            else:
                messages.error(request, 'Error updating comment!')
    else:
        messages.error(request, 'You can only edit your own comments!')

    return redirect('post_detail', slug=slug)


@login_required
def comment_delete(request, slug, comment_id):
    """
    Allows a user to delete their comment on a specific blog post.

    Only the author of the comment can delete it. A success or error message
    is displayed based on the outcome.

    Args:
        request (HttpRequest): The HTTP request object.
        slug (str): The slug of the post to which the comment belongs.
        comment_id (int): The ID of the comment to delete.

    Returns:
        HttpResponseRedirect: Redirects back to the post detail page.
    """
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.success(request, 'Comment deleted!')
    else:
        messages.error(request, 'You can only delete your own comments!')

    return redirect('post_detail', slug=slug)


def test_email(request):
    """
    Simple view to test email functionality.
    Access this via /test-email/ URL.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Response indicating success or failure of email test.
    """
    if request.user.is_superuser:
        try:
            send_mail(
                subject='Test Email from Dive In Blog',
                message='Email configuration test successful!',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[request.user.email],
                fail_silently=False,
            )
            return HttpResponse(
                """
                <h2>Email test initiated!</h2>
                <p>Check your email inbox at: {}</p>
                <p style="color: green;">Email sent successfully.</p>
                """.format(request.user.email)
            )
        except Exception as e:
            return HttpResponse(
                f"""
                <h2>Email test failed!</h2>
                <p style="color: red;">Error: {str(e)}</p>
                <p>Please check email settings.</p>
                """
            )
    return HttpResponse("Unauthorized", status=401)


@require_POST
@staff_member_required
def approve_comment(request, comment_id):
    """
    Approve a single comment via AJAX request.
    """
    try:
        comment = get_object_or_404(Comment, id=comment_id)
        comment.approved = True
        comment.save()
        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})


@require_POST
def subscribe_newsletter(request):
    """
    Handle newsletter subscription requests.
    """
    try:
        email = request.POST.get('email')
        name = request.POST.get('name', '')  # Optional name field

        if email:
            # Check if already subscribed
            if not Subscriber.objects.filter(email=email).exists():
                subscriber = Subscriber.objects.create(
                    email=email,
                    name=name,
                    active=True
                )
                messages.success(
                    request,
                    'Thank you for subscribing to our newsletter!'
                )
            else:
                messages.info(
                    request,
                    'You are already subscribed to our newsletter.'
                )
        else:
            messages.error(
                request,
                'Please provide a valid email address.'
            )

    except Exception as e:
        messages.error(
            request,
            'Sorry, there was an error processing your subscription.'
        )

    # Redirect back to the referring page
    return redirect(request.META.get('HTTP_REFERER', 'home'))


@login_required
def profile_view(request, username=None):
    """
    Display user profile page.
    If username is provided, show that user's profile.
    If not, show the logged-in user's profile.
    """
    if username:
        profile_user = get_object_or_404(User, username=username)
    else:
        profile_user = request.user

    profile = get_object_or_404(UserProfile, user=profile_user)
    user_posts = Post.objects.filter(author=profile_user).order_by('-created_on')
    user_comments = Comment.objects.filter(author=profile_user).order_by('-created_on')

    context = {
        'profile': profile,
        'user_posts': user_posts,
        'user_comments': user_comments,
    }

    return render(request, 'blog/profile.html', context)


@login_required
def edit_profile(request):
    """Handle profile editing"""
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'blog/edit_profile.html', {'form': form})
