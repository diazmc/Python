from __future__ import unicode_literals

from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=45)
    author = models.CharField(max_length=45)
    published_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=45)
    in_print = models.BooleanField()
    updated_at = models.DateTimeField(auto_now=True)