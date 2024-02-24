from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _
class Category(models.Model):
    category_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category_name = models.CharField(max_length=225)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    category_image = models.TextField(blank=True)  # Image Field to store image of the product in base
    
