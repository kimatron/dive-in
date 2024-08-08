from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin route should be at the top
    path('summernote/', include('django_summernote.urls')),  # Summernote route
    path("about/", include("about.urls"), name="about-urls"),  # About route
    path("accounts/", include("allauth.urls")),  # Accounts route
    # Blog route, should be last
    path("", include("blog.urls"), name="blog-urls"),
]
