from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_id','name','description','category','manufacturer']
        # fields = '__all__'


class PricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product       
        fields = ['product', 'price', 'offer', 'special_price']

class ProductDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product 
        fields = ['product', 'dimensions', 'color', 'material', 'style_design', 'surface_finish', 'edge_type']

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product 
        fields = ['product', 'stock_quantity', 'availability']

class VisualsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product    
        fields = ['product', 'image', 'demo_video']

class ShippingInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product 
        fields = ['product', 'shipping_weight', 'shipping_dimensions', 'special_shipping_notes']

class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product   
        fields = ['product', 'tag']

class FeaturedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product    
        fields = ['product', 'is_featured']

class SpecificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product 
        fields = ['product', 'technical_specifications', 'installation_instructions', 'maintenance_instructions', 'warranty_information']

class TaxInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product', 'tax_rate', 'tax_code', 'tax_exempt']

class ProductVariantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product', 'size_variant', 'color_variant', 'style_variant']

class RelatedProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product 
        fields = ['product', 'related_product']

class BulkPricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product', 'bulk_quantity_pricing', 'min_order_quantity']

class SalesInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product', 'sales_start_date', 'sales_end_date']

class CustomizationOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product', 'customization_choices', 'customization_fee']

class ProductReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product', 'average_rating', 'num_reviews']

class ReturnPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product', 'return_period_days', 'return_conditions']

class SalesHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product', 'sales_quantity', 'sales_revenue']

class ProductStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product', 'is_active', 'is_discontinued']

class AdminNotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product 
        fields = ['product', 'admin_notes']

class DateAddedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product     
        fields = ['product', 'date_added']

class LastModifiedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product', 'last_modified']

class UserAssignedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product', 'user_assigned']

class ApprovalStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product', 'approval_status']

class InternalProductIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product', 'internal_product_id']

class SalesRepresentativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product', 'sales_representative']

class ProductURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product 
        fields = ['product', 'product_url']

class NotificationPreferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product', 'notification_preferences']

class AuditTrailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product 
        fields = ['product', 'change_description', 'date_changed']
