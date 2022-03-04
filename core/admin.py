from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.html import format_html

from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    ordering = ['username']
    readonly_fields = ['avatar']
    list_filter = ['is_staff', 'date_joined']
    list_display = ["username", "email", "first_name", "last_name", "is_staff"]
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'username', 'email', 'phone_number', 'password1', 'password2'),

        }),
    )

    def avatar(self, obj):
        return format_html(r"<img src={} style='height: 5.5rem; width: 5.5rem; object-fit: cover' />",
                           obj.profile_picture.url) if obj.profile_picture else None

    def get_fieldsets(self, request, obj=None):
        fields = list(super(UserAdmin, self).get_fieldsets(request, obj))

        if obj is not None:
            fields[1] = (
                'Personal info',
                {'fields': ('first_name', 'last_name', 'email', 'phone_number', 'profile_picture', 'avatar')}
            )

        return fields
