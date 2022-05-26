from django.contrib.auth.models import User, Group
from rest_framework.permissions import BasePermission


class HRPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='Driver').exists():
            return True

# class HRAccessPolicy(AccessPolicy):
#     statements = [
#         {
#             "action": ["*"],
#             "principal": ["group:Administration"],
#             "effect": "deny"
#         },
#         {
#             "action": ["list", "update", "partial_update", "create"],
#             "principal": ["group:Driver"],
#             "effect": "allow"
#         },
#         {
#             "action": ["list", "*"],
#             "principal": ["*"],
#             "effect": "allow"
#         },
#     ]
