from django.db import models

from cms.models.user import User
from cms.models.post import Post

class Rating(models.Model):
    post = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey(Post, on_delete=models.CASCADE)
    post_rating = models.IntegerField()

    def __str__(self):
        return f"Rating {self.pk}"