from django.db import models
from category.models import Category
from brand.models import Brand
import uuid
# Create your models here.
class Product (models.Model):
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_name = models.CharField(max_length = 200)
    description  = models.CharField(max_length = 220)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    sku =  models.CharField(max_length=50,unique = True)
    country = models.CharField(max_length=50)
    
class Prince_and_offer(models.Model):
    price_id =models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    price = models.DecimalField(max_digits=7,decimal_places = 3)
    special_Price = models.DecimalField(max_digits=7,decimal_places = 3)
    

