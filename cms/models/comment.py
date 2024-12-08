from django.db import models
from django.utils import timezone

from cms.models.user import User
from cms.models.post import Post

class Comment(models.Model):
    """Model definition for Comment."""

    comment = models.CharField(max_length=180)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    is_hidden = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        """Unicode representation of Comment."""
        return f"Commend - {self.pk}"
