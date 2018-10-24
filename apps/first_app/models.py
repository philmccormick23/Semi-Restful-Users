from __future__ import unicode_literals
from django.db import models
from taggit.managers import TaggableManager

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = TaggableManager()

class Scores(models.Model):
    score = models.IntegerField(default=1)
    tag = models.CharField(max_length=200)
    user = models.ForeignKey(User, models.CASCADE, related_name="scores")
