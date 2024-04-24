import uuid
from django.db import models
from django.contrib.postgres.fields import ArrayField
from product.models import Product
from user.models import User

class Cart(models.Model):
    cart_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    quantity = models.PositiveIntegerField(default=1)  # Assuming a default value
    count = models.PositiveBigIntegerField(default=0)  # Assuming a default value
    total_amount = models.PositiveBigIntegerField(default=0)  # Assuming a default value # OneToOneField doesn't need a default or unique parameter
    user = models.OneToOneField(User, default=uuid.uuid4, unique=True, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    
