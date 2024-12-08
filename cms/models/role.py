from django.db import models

class Role(models.Model):
    key = models.CharField(max_length=50, unique=True)
    label = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    
    def __str__(self):
        return f"{self.key} - {self.status}"