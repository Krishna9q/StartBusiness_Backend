import uuid
from django.db import models
from user.models import User

class Address(models.Model):
    address_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=225,blank=True)
    mobile_number = models.CharField(max_length=225, unique=True)
    pincode = models.CharField(max_length=225,blank=True)
    locality = models.CharField(max_length=225,blank=True)
    address = models.TextField(blank=True)
    city = models.CharField(max_length=225,blank=True)
    state = models.CharField(max_length=225,blank=True)
    landmark = models.CharField(max_length=225,blank=True)
    alternate_mobile_number=models.CharField(max_length=225,blank=True)
    user = models.ForeignKey(User,default=uuid.uuid4,on_delete=models.CASCADE)
