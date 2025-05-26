from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an article to edit or delete it.
    """

    def has_object_permission(self, request, view, obj):
        # Allow any safe method (e.g., GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True

        # Otherwise, only allow if the user is the author of the article
        return obj.author == request.user
