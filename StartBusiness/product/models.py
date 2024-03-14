from django.db import models
from category.models import Category
from brand.models import Brand
import uuid
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class Product(models.Model):
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Brand,on_delete=models.CASCADE)
    sku = models.CharField(max_length=50, unique=True)
    country_of_origin = models.CharField(max_length=100)

      # Fields from Pricing
    price = models.DecimalField(max_digits=10,null=True, decimal_places=2)
    offer = models.CharField(max_length=255, blank=True)
    special_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    # Fields from ProductDetails
    dimensions = ArrayField(models.DecimalField(max_digits=10, decimal_places=2), null=True,size=3)
    color = models.CharField(max_length=100,blank=True)
    material = models.CharField(max_length=100,blank=True)
    style_design = models.CharField(max_length=100,blank=True)
    surface_finish = models.CharField(max_length=100,blank=True)
    edge_type = models.CharField(max_length=100,blank=True)

    # Fields from Inventory
    stock_quantity = models.PositiveIntegerField(null=True)
    availability = models.BooleanField(default=True)

    # Fields from Visuals
    image = models.ImageField(upload_to='product_images/',null=True)
    demo_video = models.URLField(null=True)

    # Fields from ShippingInformation
    shipping_weight = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    shipping_dimensions = ArrayField(models.DecimalField(max_digits=10, decimal_places=2), size=3,null=True)
    special_shipping_notes = models.TextField(blank=True)

    
    tags = models.CharField(max_length=100)

    # Fields from Featured
    is_featured = models.BooleanField(default=False)

    # Fields from Specifications
    technical_specifications = models.TextField(blank=True)
    installation_instructions = models.TextField(blank=True)
    maintenance_instructions = models.TextField(blank=True)
    warranty_information = models.TextField(blank=True)

    # Fields from TaxInformation
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2,null=True)
    tax_code = models.CharField(max_length=20,blank=True)
    tax_exempt = models.BooleanField(default=False)

    # Fields from ProductVariants
    size_variant = models.CharField(max_length=100,blank=True)
    color_variant = models.CharField(max_length=100,blank=True)
    style_variant = models.CharField(max_length=100,blank=True)

    # Fields from RelatedProducts - Assuming self-referencing relationship

    # related_products = models.ManyToManyField('self', symmetrical=False)

    # Fields from BulkPricing
    bulk_quantity_pricing = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    min_order_quantity = models.PositiveIntegerField(null=True)

    # Fields from SalesInformation
    sales_start_date = models.DateTimeField(auto_now=True)
    sales_end_date = models.DateTimeField(auto_now=True)

    # Fields from CustomizationOptions
    customization_choices = models.TextField(blank=True)
    customization_fee = models.DecimalField(max_digits=10, decimal_places=2,null=True)

    # Fields from ProductReviews
    average_rating = models.DecimalField(max_digits=3, decimal_places=2,null=True)
    num_reviews = models.PositiveIntegerField(null=True)

    # Fields from ReturnPolicy
    return_period_days = models.PositiveIntegerField(null=True)
    return_conditions = models.TextField(blank=True)

    # Fields from SalesHistory
    sales_quantity = models.PositiveIntegerField(null=True)
    sales_revenue = models.DecimalField(max_digits=15, decimal_places=2,null=True)

    # Fields from ProductStatus
    is_active = models.BooleanField(default=True)
    is_discontinued = models.BooleanField(default=False)

    # Fields from AdminNotes
    admin_notes = models.TextField(blank=True)

    # Fields from DateAdded
    date_added = models.DateTimeField(auto_now_add=True)

    # Fields from LastModified
    last_modified = models.DateTimeField(auto_now=True)

    # Fields from UserAssigned
    user_assigned = models.CharField(max_length=100,blank=True)

    # Fields from ApprovalStatus
    approval_status = models.CharField(max_length=20,blank=True)

    # Fields from InternalProductID
    internal_product_id = models.CharField(max_length=50,blank=True)

    # Fields from SalesRepresentative
    sales_representative = models.CharField(max_length=100,blank=True)

    # Fields from ProductURL
    product_url = models.URLField(blank=True)

    # Fields from NotificationPreferences
    notification_preferences = models.TextField(blank=True)

    # Fields from AuditTrail
    audit_trail = models.TextField(blank=True)
