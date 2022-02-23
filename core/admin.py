from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Profile


class ProfileInline(admin.StackedInline):
    model = Profile


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline]
    ordering = ['username']
    list_filter = ['is_staff', 'date_joined']
    list_display = ["username", "email", "first_name", "last_name", "is_staff"]
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'username', 'email', 'password1', 'password2',),

        }),
    )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ['avatar']
    list_display = ["user", "phone_number", "description", "avatar"]

    def avatar(self, obj):
        return format_html(r"<img src={} style='height: 2.5rem; width: 2.5rem; object-fit: cover' />",
                           obj.profile_picture.url) if obj.profile_picture else None
