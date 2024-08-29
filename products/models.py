from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 200, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    # photo_li
    def __str__(self):
        return self.name

