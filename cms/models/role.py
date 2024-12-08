from django.db import models
from django.utils import timezone

class Role(models.Model):
    key = models.CharField(max_length=50, unique=True)
    label = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.key} - {self.status}"