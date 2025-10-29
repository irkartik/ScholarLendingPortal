from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    """
    Custom permission to only allow admin users.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == 'admin'

class IsStaffOrAdmin(permissions.BasePermission):
    """
    Custom permission to allow staff and admin users.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role in ['staff', 'admin']

class IsOwnerOrStaff(permissions.BasePermission):
    """
    Custom permission to allow owners of an object or staff/admin.
    """
    def has_object_permission(self, request, view, obj):
        # Staff and admin can access any object
        if request.user.role in ['staff', 'admin']:
            return True

        # Check if object has a user attribute and if it matches request user
        if hasattr(obj, 'user'):
            return obj.user == request.user

        return False

