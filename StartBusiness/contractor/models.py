import uuid
from django.db import models

class Contractor(models.Model):
    contractor_id = models.UUIDField(primary_key=True, default=uuid.uuid4,unique=True, editable=False)
    contractor_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
