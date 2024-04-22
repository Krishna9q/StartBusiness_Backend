import uuid
from django.db import models
from product.models import Product
from user.models import User

class Cart(models.Model):
    cart_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False,unique=True)
    quantity = models.PositiveIntegerField()
    price = models.PositiveBigIntegerField()
    total_amount = models.PositiveBigIntegerField()
    product = models.ForeignKey(Product,default=uuid.uuid4,on_delete=models.CASCADE)
    user = models.ForeignKey(User,default=uuid.uuid4,on_delete=models.CASCADE)