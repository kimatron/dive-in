from django.shortcuts import render
from django.views import generic
from django.contrib import messages
from .models import Post
from django.shortcuts import get_object_or_404
from .models import Post
from .forms import CommentForm
from .models import FeaturedPost
# Create your views here.


class PostList(generic.ListView):
    queryset = queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blog/index.html"
    paginate_by = 5


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

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
                'Comment submitted and will be approved shortly, as long as you"re not a rudey'
            )
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
