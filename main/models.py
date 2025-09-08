from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField() # karena harga gabisa minus
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)

    stock = models.PositiveIntegerField(default=0) # karena stock gabisa minus
    brand = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
