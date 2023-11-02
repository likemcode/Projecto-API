from rest_framework import permissions
from .models import *

class IsProjectManager(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.groups.filter(name='project_managers').exists()

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)

class IsEngineer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.groups.filter(name='engineers').exists()

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view) and (
            isinstance(obj, Task) and request.user in obj.assigned_to.all()
            or isinstance(obj, TechnicalDocument) and request.user in obj.task.assigned_to.all()
        )

class IsStakeholder(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.groups.filter(name='stakeholders').exists()

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)
