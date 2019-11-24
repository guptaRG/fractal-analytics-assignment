from django.contrib.auth import get_user_model
from rest_framework import permissions


class IsUser(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if isinstance(obj, get_user_model()):
            return obj == request.user
