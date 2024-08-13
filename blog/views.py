from .forms import CommentForm
from .models import Post, Comment
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from .models import Post, FeaturedPost, Comment
# from django.http import HttpResponseForbidden
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blog/index.html"
    paginate_by = 6


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    # Filter to show only approved comments for all users
    approved_comments = post.comments.filter(approved=True)

    if request.user.is_authenticated:
        # Add the user's own unapproved comments
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
    featured_posts = FeaturedPost.objects.filter(is_featured=True)
    # Add other logic to retrieve non-featured posts or additional data

    context = {
        'featured_posts': featured_posts,
        # Add other context data as needed
    }

    return render(request, 'blog_home.html', context)


def comment_edit(request, slug, comment_id):
    """
    View to edit comments
    """
    if request.method == "POST":
        post = get_object_or_404(Post, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
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
    comments = Comment.objects.filter(
        approved=False)  # List of unapproved comments

    if request.method == 'POST':
        for comment_id in request.POST.getlist('approve'):
            comment = get_object_or_404(Comment, pk=comment_id)
            comment.approved = True
            comment.save()
        messages.success(request, 'Comments approved successfully.')
        return redirect('comment_approval')

    return render(request, 'admin/comment_approval.html', {'comments': comments})
