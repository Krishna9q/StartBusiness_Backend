import uuid
from django.db import models
from dealer.models import Dealer
from category.models import Category
from dealer.models import Dealer

class Brand(models.Model):
    brand_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    brand_name = models.CharField(max_length=225)
    brand_logo = models.TextField(blank=True)  
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(Category,default=uuid.uuid4,on_delete=models.CASCADE)
    # dealer = models.ForeignKey(Dealer,default=uuid.uuid4,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateField(auto_now=True)
    dealer = models.ManyToManyField(Dealer)


    
