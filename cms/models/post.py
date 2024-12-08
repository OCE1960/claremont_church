from django.db import models
from django.utils import timezone
from django.urls import reverse

from cms.models.user import User

class Post(models.Model):
    STATUS_CHOICES = {
    "draft": "Draft",
    "published": "Published",
    "withdrawn": "Withdrawn",
    }
    title = models.CharField(max_length=180)
    content = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    attachment = models.FileField(upload_to="attachments", default=None, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
