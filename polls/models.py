from django.db import models

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=255)
  author = models.CharField(max_length=30, default="Anonymous")
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now_add=True)