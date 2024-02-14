from django.db import models
import uuid
from django.contrib.auth.hashers import make_password

class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_email = models.EmailField(max_length=225)
    user_mobile_number = models.CharField(max_length=225)
    user_password = models.CharField(max_length=225)
    is_verify = models.BooleanField(default=False)
    user_role = models.CharField(max_length=225)
    otp_key = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
   
    # user_password = str(user_password)
    # user_password= make_password(user_password)