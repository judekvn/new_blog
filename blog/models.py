from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    url = models.URLField()
    image = models.ImageField(upload_to='blog')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
