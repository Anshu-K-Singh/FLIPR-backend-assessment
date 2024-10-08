from django.db import models
from django.contrib.auth import get_user_model
from product_app.models import Product

User = get_user_model()

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.user.username} - {self.product.name}'
