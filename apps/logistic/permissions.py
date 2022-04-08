from rest_access_policy import AccessPolicy


class HRAccessPolicy(AccessPolicy):
    statements = [
        {
            "action": ["*"],
            "principal": ["group:Administrator"],
            "effect": "deny"
        },
        {
            "action": ["list", "update", "partial_update", "create"],
            "principal": ["group:Driver"],
            "effect": "allow"
        },
    ]
