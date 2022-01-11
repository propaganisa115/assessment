from django.db import models
from django.utils.timezone import now

# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_at = models.DateTimeField(blank=True,default=now,null=True)
    created_at = models.DateTimeField(blank=True,default=now, null=True)
    updated_at = models.DateTimeField(blank=True,default=now,null=True)
