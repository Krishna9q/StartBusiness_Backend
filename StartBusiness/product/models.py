from django.db import models
from category.models import Category
from brand.models import Brand
import uuid
import random
import string
from django.contrib.postgres.fields import ArrayField
# Create your models here.


class Product(models.Model):
    
    # basic info
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    sku = models.CharField(max_length=8, unique=True,default=''.join(random.choices(string.ascii_uppercase, k=3))+''.join(random.choices(string.digits, k=5)))
    country_of_origin = models.CharField(max_length=100)

     # Fields from media
    image = models.ImageField(upload_to='product_images/',null=True)
    demo_video = models.FileField(upload_to='product_videos/',null=True)


    # Fields from ProductDetails
    dimensions = ArrayField(models.DecimalField(max_digits=10, decimal_places=2), null=True,size=3)
    color = models.CharField(max_length=100,blank=True)
    material = models.CharField(max_length=100,blank=True)
    style_design = models.CharField(max_length=100,blank=True)
    surface_finish = models.CharField(max_length=100,blank=True)
    edge_type = models.CharField(max_length=100,blank=True)

      # Fields from Pricing
    price = models.DecimalField(max_digits=10,null=True, decimal_places=2)
    offer = models.CharField(max_length=255, blank=True)
    discount = models.PositiveIntegerField(default=0)  # Percentage of
    special_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    special_price_start = models.DateTimeField(auto_now=True)
    special_price_end = models.DateTimeField(auto_now=True)

    
    # Fields from BulkPricing
    bulk_quantity_pricing = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    min_order_quantity = models.PositiveIntegerField(null=True)
    bulk_discount=models.PositiveIntegerField(default=0)

    # Fields from TaxInformation
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2,null=True)
    tax_code = models.CharField(max_length=20,blank=True)
    tax_exempt = models.BooleanField(default=False)

    # Fields from Inventory
    stock_quantity = models.PositiveIntegerField(null=True)
    availability = models.BooleanField(default=True)
    inventory_management=models.CharField(max_length=20,blank=True)


    # Fields from ProductVariants
    size_variant = models.CharField(max_length=100,blank=True)
    color_variant = models.CharField(max_length=100,blank=True)
    style_variant = models.CharField(max_length=100,blank=True)


    # additional information
    application_details = models.TextField()
    maintainance_details = models.TextField()
    privacy_policy = models.TextField()

    # seo info
    product_url = models.URLField()
    meta_title = models.CharField(max_length=255,blank=True)
    meta_description = models.TextField()
    targeted_keywords = models.CharField(max_length=255,blank=True)
    long_tail_keywords = models.TextField()

    
