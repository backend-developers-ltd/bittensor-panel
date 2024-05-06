from django.db import models  # noqa


class HyperParameter(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, unique=True)
    value = models.DecimalField(max_digits=32, decimal_places=0)
