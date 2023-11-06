from rest_framework import permissions
from .models import *

class IsProjectManager(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.groups.filter(name='project_managers').exists()

    def has_object_permission(self, request, view, obj):
        if request.method in ['PUT', 'PATCH', 'DELETE']:
            # Check if the user is a project manager
            if request.user.groups.filter(name='project_managers').exists():
                # Check if the user is the owner of the project
                return obj.owner == request.user
        return True

class IsEngineer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.groups.filter(name='engineers').exists()

    def has_object_permission(self, request, view, obj):
        if request.method in ['PUT', 'PATCH', 'DELETE']:
            # Check if the user is an engineer
            if request.user.groups.filter(name='engineers').exists():
                # Check if the user is the owner of the task
                return obj.owner == request.user
        return True


