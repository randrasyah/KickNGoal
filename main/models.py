import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    CATEGORY_CHOICES = [
        ('apparel', 'Apparel'),
        ('shoes', 'Shoes'),
        ('tshirt', 'Tshirt'),
        ('jersey', 'Jersey'),
        ('jacket', 'Jacket'),
        ('shorts', 'Shorts'),
        ('socks', 'Socks'),
        ('decker', 'Decker'),
        ('ball', 'Ball')
    ]

    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField() # karena harga gabisa minus
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='apparel')
    is_featured = models.BooleanField(default=False)

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    stock = models.PositiveIntegerField(default=0) # karena stock gabisa minus
    brand = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
    
    @property
    def is_product_hot(self):
        return self.product_views > 5
        
    def increment_views(self):
        self.product_views += 1
        self.save()