from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from .models import Post, FeaturedPost, Comment
from django.http import HttpResponseRedirect
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
# Create your views here.


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blog/index.html"
    paginate_by = 6


def post_detail(request, slug):
    post = get_object_or_404(Post, status=1, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and will be approved shortly, as long as you\'re not a rudey'
            )
            return redirect('post_detail', slug=slug)
    else:
        comment_form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )


def blog_home(request):
    featured_posts = FeaturedPost.objects.filter(is_featured=True)
    # Add other logic to retrieve non-featured posts or additional data

    context = {
        'featured_posts': featured_posts,
        # Add other context data as needed
    }

    return render(request, 'blog_home.html', context)


@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    # Ensure the user is the author or staff
    if comment.author != request.user and not request.user.is_staff:
        return redirect('post_detail', slug=comment.post.slug)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post_detail', slug=comment.post.slug)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'blog/edit_comment.html', {'form': form, 'comment': comment})


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    # Ensure the user is the author or staff
    if comment.author != request.user and not request.user.is_staff:
        return redirect('post_detail', slug=comment.post.slug)

    if request.method == 'POST':
        comment.delete()
        return redirect('post_detail', slug=comment.post.slug)

    return render(request, 'blog/delete_comment.html', {'comment': comment})
