from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        return request.user == obj.creator

    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return request.user.is_authenticated


