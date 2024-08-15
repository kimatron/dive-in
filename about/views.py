from django.shortcuts import render, redirect
from django.contrib import messages
from .models import About
from .forms import CollaborateForm


def about_page(request):
    """
    Renders the 'About' page, displaying the most recent information about the company.

    Retrieves the latest 'About' instance from the database (ordered by the most recently updated)
    and passes it to the 'about.html' template for rendering.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered 'about.html' template with the context containing the 'About' instance.
    """
    about = About.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "about/about.html",
        {"about": about},
    )


def about_view(request):
    print("About view is being called")
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

    return render(
        request,
        'about/about.html',
        {
            'about': about,
            'collaborate_form': form,
        }
    )
