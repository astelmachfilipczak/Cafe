from rest_framework.permissions import BasePermission

class IsCashierUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.role >=0)

class IsBaristaUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.role >= 2)

class IsManagerUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.role >= 3)

class IsOwnerUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.role == 4 or request.user.is_superuser)