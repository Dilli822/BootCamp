

from rest_framework.permissions import BasePermission

# let's make custom permission user files

class IsStaffUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_staff
