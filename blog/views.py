from .forms import CommentForm
from .models import Post, Comment
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from .models import Post, FeaturedPost, Comment
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse


class PostList(generic.ListView):
    """
    Displays a paginated list of published blog posts.

    Attributes:
        queryset (QuerySet): The queryset of published posts ordered by creation date (most recent first).
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
    approved_comments = post.comments.filter(approved=True)

    if request.user.is_authenticated:
        user_comments = post.comments.filter(author=request.user)
        comments = list(approved_comments) + list(user_comments)
    else:
        comments = approved_comments

    comment_count = len(comments)

    if request.method == 'POST' and request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.approved = False  # Mark as unapproved by default
            comment.save()
            messages.success(
                request, 'Your comment has been submitted and is awaiting approval.')
            return HttpResponseRedirect(reverse('post_detail', args=[slug]))
    else:
        comment_form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'comment_count': comment_count,
        'comment_form': comment_form,
        'user': request.user,
    }
    return render(request, 'blog/post_detail.html', context)


def blog_home(request):
    """
    Displays the blog homepage with featured posts.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered template for the blog homepage with featured posts.
    """
    featured_posts = FeaturedPost.objects.filter(is_featured=True)

    context = {
        'featured_posts': featured_posts,
    }

    return render(request, 'blog_home.html', context)


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
    if request.method == "POST":
        post = get_object_or_404(Post, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False  # Mark as unapproved by default
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


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
    post = get_object_or_404(Post, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.success(request, 'Comment deleted!')
    else:
        messages.error(request, 'You can only delete your own comments!')

    return redirect('post_detail', slug=slug)


@staff_member_required
def comment_approval(request):
    """
    Displays a list of unapproved comments for admin approval.

    Admins can approve multiple comments at once. Once approved, the comments
    are marked as such and saved.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered template displaying the list of unapproved comments.
    """
    comments = Comment.objects.filter(approved=False)

    if request.method == 'POST':
        for comment_id in request.POST.getlist('approve'):
            comment = get_object_or_404(Comment, pk=comment_id)
            comment.approved = True
            comment.save()
        messages.success(request, 'Comments approved successfully.')
        return redirect('comment_approval')

    return render(request, 'admin/comment_approval.html', {'comments': comments})


def test_email(request):
    """
    Simple view to test email functionality.
    Access this via /test-email/ URL.
    """
    if request.user.is_superuser:  # Only allow superusers to test
        try:
            send_mail(
                subject='Test Email from Dive In Blog',
                message='If you see this, your email configuration is working!',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[request.user.email],  # Sends to the logged-in superuser's email
                fail_silently=False,
            )
            return HttpResponse(
                """
                <h2>Email test initiated!</h2>
                <p>Check your email inbox at: {}</p>
                <p style="color: green;">If no errors appeared, the email was sent successfully.</p>
                """.format(request.user.email)
            )
        except Exception as e:
            return HttpResponse(
                f"""
                <h2>Email test failed!</h2>
                <p style="color: red;">Error: {str(e)}</p>
                <p>Check your email settings and try again.</p>
                """
            )
    else:
        return HttpResponse("Unauthorized", status=401)
