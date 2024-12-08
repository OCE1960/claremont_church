from django.db import models

from cms.models.role import Role
from cms.models.user import User

class RoleUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=True)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return f"RoleUser {self.pk}" 
