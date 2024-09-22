from django.db import models

# Create your models here.

class A(models.Model):
    name = models.CharField(max_length=200)
    value = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
