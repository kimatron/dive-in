from django.contrib import admin
from .models import About, CollaborateRequest
from django_summernote.admin import SummernoteModelAdmin


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)
# Register your models here.


class CollaborateRequestAdmin(admin.ModelAdmin):
    # Remove 'created_on' if not applicable
    list_display = ('name', 'email', 'message', 'read')

    list_filter = ('read',)
    search_fields = ('name', 'email', 'message')


admin.site.register(CollaborateRequest, CollaborateRequestAdmin)
