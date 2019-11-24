from django.contrib.auth import get_user_model
from rest_framework import permissions

from bucket.models import Bucket
from to_do.models import ToDo


class IsUser(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if isinstance(obj, get_user_model()):
            return obj == request.user
        if isinstance(obj, Bucket):
            return obj.user == request.user
        if isinstance(obj, ToDo):
            return obj.bucket.user == request.user
