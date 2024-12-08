from django.db import models
from django.urls import reverse

from cms.models.user import User
from cms.models.category import Category

class Post(models.Model):
    STATUS_CHOICES = {
    "draft": "Draft",
    "published": "Published",
    "withdrawn": "Withdrawn",
    }
    title = models.CharField(max_length=180)
    content = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    attachment = models.FileField(upload_to="attachments", default=None, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("cms:post-detail", kwargs={"pk": self.pk})
