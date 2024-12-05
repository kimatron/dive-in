from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Count
from .models import About
from .forms import CollaborateForm
from blog.models import Post, Comment
from django.contrib.auth.models import User


def about_page(request):
    """
    Renders the 'About' page,
    displaying the most recent information about the company.

    Retrieves the latest 'About' instance from the database
    (ordered by the most recently updated)
    and passes it to the 'about.html' template for rendering.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered 'about.html' template
        with the context containing the 'About' instance.
    """
    about = About.objects.all().order_by('-updated_on').first()

    # Calculate statistics if about instance exists
    if about:
        total_posts = Post.objects.filter(status=1).count()
        total_authors = User.objects.filter(blog_posts__isnull=False).distinct().count()
        total_comments = Comment.objects.filter(approved=True).count()
        categories_count = Post.objects.filter(status=1).values('category').distinct().count()

        # Update the About object with new statistics
        about.articles_written = total_posts
        about.total_divers = total_authors
        about.dive_locations = categories_count
        about.save()

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "total_comments": Comment.objects.filter(approved=True).count(),
        },
    )


def about_view(request):
    """
    Handles the 'About' page view, including form submissions for collaboration requests.

    If the request method is POST and the collaboration form is valid, the request is saved,
    and a success message is shown. The user is then redirected back to the 'About' page.
    If the method is GET, the form is initialized empty, and the page is rendered with the form
    and the most recent 'About' instance.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered 'about.html' template with the context containing
                      the 'About' instance and the collaboration form.
    """
    print("About view is being called")

    if request.method == 'POST':
        form = CollaborateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your collaboration request has been submitted!')
            return redirect('about')
    else:
        form = CollaborateForm()

    about = About.objects.all().order_by('-updated_on').first()

    # Calculate statistics if about instance exists
    if about:
        total_posts = Post.objects.filter(status=1).count()
        total_authors = User.objects.filter(blog_posts__isnull=False).distinct().count()
        total_comments = Comment.objects.filter(approved=True).count()
        categories_count = Post.objects.filter(status=1).values('category').distinct().count()

        # Update the About object with new statistics
        about.articles_written = total_posts
        about.total_divers = total_authors
        about.dive_locations = categories_count
        about.save()

    return render(
        request,
        'about/about.html',
        {
            'about': about,
            'collaborate_form': form,
            'total_comments': Comment.objects.filter(approved=True).count(),
        }
    )
