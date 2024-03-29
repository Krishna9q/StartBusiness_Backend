from django.db import models
import uuid
from product.models import Product

# Create your models here.

class Stock(models.Model):
    stock_id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    product_id = models.OneToOneField(Product, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Product, on_delete=models.CASCADE,default=True) 
    current_stock = models.PositiveBigIntegerField()
    unit = models.PositiveBigIntegerField()
    default_price = models.FloatField()
    regular_selling_price = models.FloatField()
    regular_buying_price = models.FloatField()
    mrp = models.FloatField()
    stock_status = models.BooleanField(default=False)
    


