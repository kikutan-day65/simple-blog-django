from django.db import models
from datetime import datetime

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=10000000)
    ceated_at = models.DateTimeField(default=datetime.now, blank=True)
    