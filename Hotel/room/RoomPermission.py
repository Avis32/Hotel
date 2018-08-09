from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request in permissions.SAFE_METHODS:
            return True
        if permissions.IsAdminUser:
            return True
        else:
            return False

