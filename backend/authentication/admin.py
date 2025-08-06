from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User

    list_display = ("id", "username", "telegram_id", "is_staff", "is_admin", "created_at")
    search_fields = ("username", "telegram_id")
    ordering = ("-created_at",)
    list_filter = ("is_staff", "is_admin")

    readonly_fields = ("telegram_id",)

    fieldsets = list(UserAdmin.fieldsets) + [
        ("Дополнительная информация", {"fields": ("telegram_id",)}),
    ]
    add_fieldsets = list(UserAdmin.add_fieldsets) + [
        ("Дополнительная информация", {"fields": ("telegram_id",)}),
    ]