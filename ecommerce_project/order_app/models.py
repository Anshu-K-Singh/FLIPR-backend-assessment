from django.db import models
from django.contrib.auth import get_user_model
from cart_app.models import Cart

User = get_user_model()

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    cart_items = models.ManyToManyField(Cart)

    def __str__(self):
        return f'Order {self.id} by {self.user.username}'
