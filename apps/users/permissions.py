from rest_framework import permissions


class IsOwnerOrReadOnlyForAccount(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.user == request.user


class IsAdminUserForAccount(permissions.IsAdminUser):
    def has_permission(self, request, view):
        return bool(request.user.is_superuser and request.user.is_admin)