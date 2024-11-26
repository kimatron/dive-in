from . import views
from django.urls import path
# from .views import approve_comment
# from .views import comment_edit, comment_delete

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/<str:username>/', views.profile_view, name='user_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('post/<slug:slug>/comment_edit/<int:comment_id>/',
         views.comment_edit, name='comment_edit'),
    path('post/<slug:slug>/comment_delete/<int:comment_id>/',
         views.comment_delete, name='comment_delete'),
    path('approve-comment/<int:comment_id>/',
         views.approve_comment, name='approve_comment'),
    path('test-email/', views.test_email, name='test_email'),
    path('subscribe/', views.subscribe_newsletter, name='subscribe'),
]
