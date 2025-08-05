from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User

    list_display = ("id", "username", "vk_user_id", "email", "is_staff", "created_at")
    search_fields = ("username", "vk_user_id", "email")
    ordering = ("-created_at",)

    fieldsets = list(UserAdmin.fieldsets) + [
        (None, {"fields": ("vk_user_id", "height", "weight")}),
    ]
    add_fieldsets = list(UserAdmin.add_fieldsets) + [
        (None, {"fields": ("vk_user_id", "height", "weight")}),
    ]