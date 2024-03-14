from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_id','name','description','category','manufacturer','sku','country_of_origin']

# Serielizer for getting full details 
class ProductFullDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductPricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product       
        fields = ['price', 'offer', 'special_price']

class ProductDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product 
        fields = ['dimensions', 'color', 'material', 'style_design', 'surface_finish', 'edge_type']

class ProductInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product 
        fields = ['stock_quantity', 'availability']

class ProductVisualsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product    
        fields = ['image', 'demo_video']

class ProductShippingInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product 
        fields = ['shipping_weight', 'shipping_dimensions', 'special_shipping_notes']

class ProducttagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product   
        fields = [ 'tag']

class ProductFeaturedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product    
        fields = ['is_featured']

class ProductSpecificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product 
        fields = ['technical_specifications', 'installation_instructions', 'maintenance_instructions', 'warranty_information']

class ProductTaxInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['tax_rate', 'tax_code', 'tax_exempt']

class ProductVariantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['size_variant', 'color_variant', 'style_variant']

# class RelatedProductsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product 
#         fields = ['related_product']

class BulkPricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['bulk_quantity_pricing', 'min_order_quantity']

class SalesInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['sales_start_date', 'sales_end_date']

class CustomizationOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['customization_choices', 'customization_fee']

class ProductReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['average_rating', 'num_reviews']

class ReturnPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['return_period_days', 'return_conditions']

class SalesHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['sales_quantity', 'sales_revenue']

class ProductStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['is_active', 'is_discontinued']

class AdminNotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product 
        fields = ['admin_notes']

class DateAddedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product     
        fields = ['date_added']

class LastModifiedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['last_modified']

class UserAssignedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['user_assigned']

class ApprovalStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['approval_status']

class InternalProductIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['internal_product_id']

class SalesRepresentativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['sales_representative']

class ProductURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product 
        fields = ['product_url']

class NotificationPreferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['notification_preferences']

class AuditTrailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product 
        fields = ['product', 'change_description', 'date_changed']
