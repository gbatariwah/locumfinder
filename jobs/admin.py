from django.contrib import admin
from .models import Job, Comment


class CommentsInline(admin.StackedInline):
    model = Comment
    extra = 0


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    inlines = [CommentsInline]
    search_fields = ['title', 'description']
    ordering = ['created_at']
    list_filter = ['type', 'created_at', 'region', 'posted_by']
    list_display = ['title', 'type', 'region', 'posted_by']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ['comment']
    ordering = ['created_at']
    list_filter = ['created_at', 'user']
    list_display = ['message', 'job', 'user']

