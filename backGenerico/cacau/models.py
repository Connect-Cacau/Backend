from django.db import models

# Create your models here.
class Cacau(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=250, blank=True, default='')
    cacauCategory = models.CharField(max_length=200, blank=False,
default='')
    