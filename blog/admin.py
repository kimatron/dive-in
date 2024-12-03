from django.contrib import admin
from .models import (
    Post,
    Comment,
    Category,
    Tag,
    Subscriber,
    UserProfile,
    FeaturedPost,
    CertificationLevel,
)

from django_summernote.admin import SummernoteModelAdmin


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'experience_level',
        'total_dives',
        'certification_level',
        'location',
        'available_for_buddy'
    )

    list_filter = (
        'experience_level',
        'certification_level',
        'preferred_diving_type',
        'own_equipment',
        'available_for_buddy'
    )

    search_fields = (
        'user__username',
        'location',
        'favorite_dive_site',
        'certification_number'
    )

    readonly_fields = ('created_on', 'updated_on')

    fieldsets = (
        ('Basic Information', {
            'fields': (
                'user',
                'profile_picture',
                'bio',
                'location'
            )
        }),
        ('Certification Details', {
            'fields': (
                'certification_level',
                'certification_date',
                'certification_number'
            )
        }),
        ('Diving Experience', {
            'fields': (
                'experience_level',
                'total_dives',
                'diving_since',
                'max_depth_reached'
            )
        }),
        ('Diving Preferences', {
            'fields': (
                'preferred_diving_type',
                'favorite_dive_site',
                'favorite_marine_life',
            )
        }),
        ('Equipment', {
            'fields': (
                'own_equipment',
                'equipment_details',
            ),
            'classes': ('collapse',)
        }),
        ('Availability', {
            'fields': (
                'available_for_buddy',
            )
        }),
        ('Social Media', {
            'fields': (
                'instagram',
                'facebook',
                'twitter'
            ),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': (
                'created_on',
                'updated_on'
            ),
            'classes': ('collapse',)
        })
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:  # Editing an existing object
            return self.readonly_fields + ('user',)
        return self.readonly_fields


admin.site.register(CertificationLevel)


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created_on', 'approved')
    list_filter = ('approved',)
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
        self.message_user(request, "Selected comments have been approved.")

    approve_comments.short_description = "Approve selected comments"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ['name', 'description']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'subscribed_on', 'active')
    list_filter = ('active', 'subscribed_on')
    search_fields = ['email', 'name']


admin.site.register(FeaturedPost)
