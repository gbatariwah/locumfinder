from django.contrib import admin

from .models import User, Profile


class ProfileInline(admin.StackedInline):
    model = Profile


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = [ProfileInline]
    ordering = ['username']
    list_filter = ['is_staff', 'date_joined']
    list_display = ["username", "email", "first_name", "last_name", "is_staff"]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "phone_number", "description",]
