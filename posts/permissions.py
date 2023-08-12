from rest_framework import permissions

class CustomReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':  # Allow GET requests for everyone
            return True
        elif request.method == 'POST' and request.user.is_authenticated:  # Allow POST requests for authenticated users
            return True
        return False
        
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:  # Allow SAFE_METHODS (GET, HEAD, OPTIONS) for everyone
            return True
        return obj.author == request.user  # Allow editing only for the author of the post
