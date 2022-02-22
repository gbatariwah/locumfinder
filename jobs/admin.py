from django.contrib import admin
from .models import Job, Comment


# Register your models here.
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

