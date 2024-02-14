import uuid
from django.db import models

from user.models import User

class Brand(models.Model):
    brand_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,unique = True)
    brand_name = models.CharField(max_length=225)
    brand_logo = models.ImageField(upload_to= 'brand/')
    brand_status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
