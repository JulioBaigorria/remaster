from django.contrib.auth.models import User, Group
from rest_framework.permissions import BasePermission


class HRPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='Logistic').exists():
            return True
        if request.method == 'DELETE':
            if request.user.groups.filter(name='Driver').exists():
                return False
