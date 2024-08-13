from . import views
from django.urls import path
from .views import edit_comment, delete_comment

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]
