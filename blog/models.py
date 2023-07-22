from typing import Iterable, Optional
from django.db import models
from django.conf import settings
from django.utils.text import slugify


# Create your models here.
class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = "DF", "Draft"
        PUBLISHED = "PB", "Published"

    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="blog_posts"
    )

    body = models.TextField()
    image = models.ImageField(upload_to="blog/image")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.DRAFT
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ["-status"]
        indexes = [
            models.Index(fields=["-status"]),
        ]

    def __str__(self):
        return self.title


class Category(models.Model):
    pass
