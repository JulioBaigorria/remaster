from rest_framework.permissions import BasePermission


class ClientPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='Logistic').exists() or \
            request.user.groups.filter(name='Client').exists() or \
                request.user.groups.filter(name='Administration').exists():
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
