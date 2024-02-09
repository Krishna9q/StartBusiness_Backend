import uuid
from django.db import models

# Create your models here.
class Manager(models.Model):
    manager_id =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,unique = True)
    manager_name = models.CharField(max_length=225)
    manager_email = models.EmailField(max_length=225, unique=True)
    manager_mobile_number = models.CharField(max_length=10,unique=True)
    manager_address = models.TextField(blank=True)

