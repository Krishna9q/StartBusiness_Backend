import uuid
from django.db import models
from category.models import Category

class Brand(models.Model):
    brand_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,unique = True)
    brand_name = models.CharField(max_length=225)
    brand_logo = models.ImageField(upload_to= 'brand/')
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(Category,default=uuid.uuid4,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateField(auto_now=True)

    
