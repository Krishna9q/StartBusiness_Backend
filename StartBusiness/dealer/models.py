import uuid
from django.db import models

class Dealer(models.Model):
    dealer_id =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    dealer_name = models.CharField(max_length=225)
    is_active = models.BooleanField(default=True)
    dealer_email = models.EmailField(max_length=225,unique=True)
    dealer_mobile_number = models.CharField(max_length=10,unique=True)
    dealer_address = models.TextField(blank=True)
    dealer_landmark = models.TextField(blank=True)
    dealer_image = models.ImageField(upload_to='dealer/',null=True)
    dealer_description = models.TextField(blank=True)
    
