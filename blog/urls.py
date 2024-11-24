from . import views
from django.urls import path
from .views import comment_approval
# from .views import comment_edit, comment_delete

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('post/<slug:slug>/comment_edit/<int:comment_id>/',
         views.comment_edit, name='comment_edit'),
    path('post/<slug:slug>/comment_delete/<int:comment_id>/',
         views.comment_delete, name='comment_delete'),
    path('admin/comments/approve/', comment_approval, name='comment_approval'),
    path('test-email/', views.test_email, name='test_email'),
]
