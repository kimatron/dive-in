from django.shortcuts import render
from django.views import generic
from .models import Post
from django.shortcuts import get_object_or_404
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

    post = Post.objects.filter(status=1).get(slug=slug)
    
    return render(
        request,
        "blog/post_detail.html",
        {"post": post},
    )