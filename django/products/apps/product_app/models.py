from __future__ import unicode_literals

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField()
    weight = models.CharField(max_length=45)
    price = models.IntegerField()
    cost = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

