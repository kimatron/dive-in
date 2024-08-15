from . import views
from django.urls import path
from .views import about_view

urlpatterns = [
    path('', views.about_page, name='about'),
    path('about/', about_view, name='about'),
]
