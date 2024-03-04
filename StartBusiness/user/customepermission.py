
from rest_framework.permissions import BasePermission

# 

class IsManager(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        
        return request.user.user_role.lower() == "manager"
            