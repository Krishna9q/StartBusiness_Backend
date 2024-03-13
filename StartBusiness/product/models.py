from django.db import models
from category.models import Category
from brand.models import Brand
import uuid
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class Product(models.Model):
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Brand,on_delete=models.CASCADE)
    sku = models.CharField(max_length=50, unique=True)
    country_of_origin = models.CharField(max_length=100)

      # Fields from Pricing
    price = models.DecimalField(max_digits=10, decimal_places=2)
    offer = models.CharField(max_length=255)
    special_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    # Fields from ProductDetails
    dimensions = ArrayField(models.DecimalField(max_digits=10, decimal_places=2), size=3)
    color = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    style_design = models.CharField(max_length=100)
    surface_finish = models.CharField(max_length=100)
    edge_type = models.CharField(max_length=100)

    # Fields from Inventory
    stock_quantity = models.PositiveIntegerField()
    availability = models.BooleanField(default=True)

    # Fields from Visuals
    image = models.ImageField(upload_to='product_images/')
    demo_video = models.URLField()

    # Fields from ShippingInformation
    shipping_weight = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_dimensions = ArrayField(models.DecimalField(max_digits=10, decimal_places=2), size=3)
    special_shipping_notes = models.TextField()

    # Fields from Tags
    tags = models.ManyToManyField('Tag')

    # Fields from Featured
    is_featured = models.BooleanField(default=False)

    # Fields from Specifications
    technical_specifications = models.TextField()
    installation_instructions = models.TextField()
    maintenance_instructions = models.TextField()
    warranty_information = models.TextField()

    # Fields from TaxInformation
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2)
    tax_code = models.CharField(max_length=20)
    tax_exempt = models.BooleanField(default=False)

    # Fields from ProductVariants
    size_variant = models.CharField(max_length=100)
    color_variant = models.CharField(max_length=100)
    style_variant = models.CharField(max_length=100)

    # Fields from RelatedProducts - Assuming self-referencing relationship
    related_products = models.ManyToManyField('self', symmetrical=False)

    # Fields from BulkPricing
    bulk_quantity_pricing = models.DecimalField(max_digits=10, decimal_places=2)
    min_order_quantity = models.PositiveIntegerField()

    # Fields from SalesInformation
    sales_start_date = models.DateTimeField()
    sales_end_date = models.DateTimeField()

    # Fields from CustomizationOptions
    customization_choices = models.TextField()
    customization_fee = models.DecimalField(max_digits=10, decimal_places=2)

    # Fields from ProductReviews
    average_rating = models.DecimalField(max_digits=3, decimal_places=2)
    num_reviews = models.PositiveIntegerField()

    # Fields from ReturnPolicy
    return_period_days = models.PositiveIntegerField()
    return_conditions = models.TextField()

    # Fields from SalesHistory
    sales_quantity = models.PositiveIntegerField()
    sales_revenue = models.DecimalField(max_digits=15, decimal_places=2)

    # Fields from ProductStatus
    is_active = models.BooleanField(default=True)
    is_discontinued = models.BooleanField(default=False)

    # Fields from AdminNotes
    admin_notes = models.TextField()

    # Fields from DateAdded
    date_added = models.DateTimeField(auto_now_add=True)

    # Fields from LastModified
    last_modified = models.DateTimeField(auto_now=True)

    # Fields from UserAssigned
    user_assigned = models.CharField(max_length=100)

    # Fields from ApprovalStatus
    approval_status = models.CharField(max_length=20)

    # Fields from InternalProductID
    internal_product_id = models.CharField(max_length=50)

    # Fields from SalesRepresentative
    sales_representative = models.CharField(max_length=100)

    # Fields from ProductURL
    product_url = models.URLField()

    # Fields from NotificationPreferences
    notification_preferences = models.TextField()

    # Fields from AuditTrail
    audit_trail = models.TextField()
