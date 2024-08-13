from django.contrib import admin
from .models import Post, Comment, Category, Tag, Subscriber, UserProfile, FeaturedPost
from django_summernote.admin import SummernoteModelAdmin


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_picture', 'bio')
    search_fields = ('user__username', 'bio')


admin.site.register(UserProfile, UserProfileAdmin)


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
