from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    interests = models.ManyToManyField(Interest, related_name='liked by')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Interest(models.Model):
    name = models.CharField(max_length=100)
    user_id = models.ManyToManyField(User)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
