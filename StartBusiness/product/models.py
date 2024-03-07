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
    category = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    sku = models.CharField(max_length=50, unique=True)
    country_of_origin = models.CharField(max_length=100)

class Pricing(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    offer = models.CharField(max_length=255)
    special_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

class ProductDetails(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    dimensions = ArrayField(models.DecimalField(max_digits=10, decimal_places=2), size=3)
    color = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    style_design = models.CharField(max_length=100)
    surface_finish = models.CharField(max_length=100)
    edge_type = models.CharField(max_length=100)

class Inventory(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    stock_quantity = models.PositiveIntegerField()
    availability = models.BooleanField(default=True)

class Visuals(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')
    demo_video = models.URLField()

class ShippingInformation(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    shipping_weight = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_dimensions = ArrayField(models.DecimalField(max_digits=10, decimal_places=2), size=3)
    special_shipping_notes = models.TextField()

class Tags(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    tag = models.CharField(max_length=100)

class Featured(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    is_featured = models.BooleanField(default=False)

class Specifications(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    technical_specifications = models.TextField()
    installation_instructions = models.TextField()
    maintenance_instructions = models.TextField()
    warranty_information = models.TextField()

class TaxInformation(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2)
    tax_code = models.CharField(max_length=20)
    tax_exempt = models.BooleanField(default=False)

class ProductVariants(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size_variant = models.CharField(max_length=100)
    color_variant = models.CharField(max_length=100)
    style_variant = models.CharField(max_length=100)

class RelatedProducts(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='related_products')
    related_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='related_to')

class BulkPricing(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    bulk_quantity_pricing = models.DecimalField(max_digits=10, decimal_places=2)
    min_order_quantity = models.PositiveIntegerField()

class SalesInformation(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    sales_start_date = models.DateTimeField()
    sales_end_date = models.DateTimeField()

class CustomizationOptions(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    customization_choices = models.TextField()
    customization_fee = models.DecimalField(max_digits=10, decimal_places=2)

class ProductReviews(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    average_rating = models.DecimalField(max_digits=3, decimal_places=2)
    num_reviews = models.PositiveIntegerField()

class ReturnPolicy(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    return_period_days = models.PositiveIntegerField()
    return_conditions = models.TextField()

class SalesHistory(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    sales_quantity = models.PositiveIntegerField()
    sales_revenue = models.DecimalField(max_digits=15, decimal_places=2)

class ProductStatus(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_discontinued = models.BooleanField(default=False)

class AdminNotes(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    admin_notes = models.TextField()

class DateAdded(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

class LastModified(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    last_modified = models.DateTimeField(auto_now=True)

class UserAssigned(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    user_assigned = models.CharField(max_length=100)

class ApprovalStatus(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    approval_status = models.CharField(max_length=20)

class InternalProductID(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    internal_product_id = models.CharField(max_length=50)

class SalesRepresentative(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    sales_representative = models.CharField(max_length=100)

class ProductURL(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    product_url = models.URLField()

class NotificationPreferences(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    notification_preferences = models.TextField()

class AuditTrail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    change_description = models.TextField()
    date_changed = models.DateTimeField(auto_now_add=True)











# class Product (models.Model):
#     product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     product_name = models.CharField(max_length = 200)
#     description  = models.CharField(max_length = 220)
#  # category = models.ForeignKey(Category,default= uuid.uuid4,on_delete=models.CASCADE)
#     # brand = models.ForeignKey(Brand,default=uuid.uuid4,on_delete=models.CASCADE)
#     sku =  models.CharField(max_length=50,unique = True)
#     country = models.CharField(max_length=50)
    
# class Prince_and_Offer(models.Model):
#     price_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

#     # price = models.DecimalField(max_digits=7,decimal_places = 3)
#     # special_Price = models.DecimalField(max_digits=7,decimal_places = 3)
#     # product_id = models.ForeignKey(Product)
# class Product_Details(models.Model):
#     product_details = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

# class Inventory_And_Stock(models.Model):
#     inventory_and_stock_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

# class Visuals(models.Model):
#     visuals = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

# class Additional_Information(models.Model):
#     additional_information = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

# class Specifications_And_Instructions(models.Model):
#     specifications_and_instructions = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

# class Tax_Information(models.Model):
#     tax_information = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

# class Product_Variants(models.Model):
#     product_variants = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

