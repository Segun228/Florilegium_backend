import os

from rest_framework import permissions
from dotenv import load_dotenv

load_dotenv()


admin_one = os.getenv("ADMIN_1")
admin_two = os.getenv("ADMIN_2")
debug = os.getenv("DEBUG")

admins = [admin_one, admin_two]

class IsAdminOrDebugOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.telegram_id in admins or debug