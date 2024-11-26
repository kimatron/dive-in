from django.contrib import admin
from .models import About, CollaborateRequest
from django_summernote.admin import SummernoteModelAdmin


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'updated_on')
    fieldsets = (
        ('Basic Information', {
            'fields': ('company_name', 'founding_date')
        }),
        ('Hero Section', {
            'fields': ('hero_title', 'hero_subtitle', 'hero_image')
        }),
        ('Content', {
            'fields': ('mission', 'vision', 'offerings', 'content')
        }),
        ('Statistics', {
            'fields': ('total_divers', 'dive_locations', 'articles_written')
        }),
        ('Contact Information', {
            'fields': ('contact_email', 'contact_phone', 'location')
        }),
    )


class CollaborateRequestAdmin(admin.ModelAdmin):
    # Remove 'created_on' if not applicable
    list_display = ('name', 'email', 'message', 'read')

    list_filter = ('read',)
    search_fields = ('name', 'email', 'message')


admin.site.register(CollaborateRequest, CollaborateRequestAdmin)
