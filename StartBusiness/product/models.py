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
    category_id = models.ForeignKey(Category,on_delete=models.CASCADE)
    brand_id = models.ForeignKey(Brand,on_delete=models.CASCADE)
    sku = models.CharField(max_length=8, unique=True,default=''.join(random.choices(string.ascii_uppercase, k=3))+''.join(random.choices(string.digits, k=5)))
    country_of_origin = models.CharField(max_length=100)


     # Fields from media
    image = models.ImageField(upload_to='product_images/')
    image1 = models.ImageField(upload_to='product_images/',null=True)
    image2 = models.ImageField(upload_to='product_images/',null=True)
    image3 = models.ImageField(upload_to='product_images/',null=True)
    image4 = models.ImageField(upload_to='product_images/',null=True)
    image5 = models.ImageField(upload_to='product_images/',null=True)
    demo_video = models.FileField(upload_to='product_videos/',null=True)


    # Fields from ProductDetails
    length = models.FloatField(null = True, blank=True)
    width = models.FloatField(null = True, blank=True)
    thickness = models.FloatField(null = True, blank=True)
    weight = models.FloatField(null = True, blank=True)
    color = models.CharField(max_length=100,blank=True)
    material = models.CharField(max_length=100,blank=True)
    style_design = models.CharField(max_length=100,blank=True)
    surface_finish = models.CharField(max_length=100,blank=True)
    edge_type = models.CharField(max_length=100,blank=True)
    sq_ft_box  = models.DecimalField(max_digits=10,null=True, decimal_places=2)
    no_of_pcs_box = models.IntegerField(null=True,blank=True)
    product_collections = models.CharField(max_length=10000,blank=True, null=True)
    label = models.CharField(max_length=10000,blank=True, null=True)
    layout = models.CharField(max_length=10000,blank=True, null=True)



      # Fields from Pricing
    price = models.DecimalField(max_digits=10,null=True, decimal_places=2)
    discount = models.FloatField(null = True, blank=True)
    offer_type = models.CharField(max_length=255, blank=True)
    discount = models.PositiveIntegerField(default=0)  # Percentage of
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount_price_start = models.DateTimeField()
    discount_price_end = models.DateTimeField()

    
    # Fields from BulkPricing
    bulk_quantity_pricing = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    min_order_quantity = models.PositiveIntegerField(null=True)
    bulk_discount=models.PositiveIntegerField(default=0)

    # Fields from TaxInformation
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2,null=True)
    tax_code = models.CharField(max_length=20,blank=True)
    tax_class = models.CharField(max_length=225,blank=True)

    # Fields from Inventory
    stock_quantity = models.PositiveIntegerField(null=True)
    availability = models.BooleanField(default=True)
   


    # Fields from ProductVariants
    size_variant = ArrayField(models.CharField(max_length=100,blank=True))
    color_variant =  ArrayField(models.CharField(max_length=100,blank=True))
    style_variant = ArrayField(models.CharField(max_length=100,blank=True))
    related_product = ArrayField(models.CharField(max_length=100,blank=True))
    cross_selling_product= ArrayField(models.CharField(max_length=100,blank=True))


    # additional information
    product_use = models.TextField(blank=True)
    maintainance_details = models.TextField()
    privacy_policy = models.TextField()

    # seo info
    product_url = models.URLField()
    meta_title = models.CharField(max_length=255,blank=True)
    meta_description = models.TextField()
    featured_keywords = models.CharField(max_length=255,blank=True)
    long_tail_keywords = models.TextField()
    status = models.CharField(max_length = 50, choices=(('Published', 'Published'),('Draft', 'Draft'),('Pending','Pending')))
    is_featured = models.BooleanField()

    
