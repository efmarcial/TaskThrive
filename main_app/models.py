from django.db import models

# Create your models here.
class Service(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    
    class Meta:
        ordering = ['created']