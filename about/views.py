from django.shortcuts import render, redirect
from django.contrib import messages
from .models import About
from .forms import CollaborateForm


def about_page(request):
    about = About.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "about/about.html",
        {"about": about},
    )


def about_view(request):
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
