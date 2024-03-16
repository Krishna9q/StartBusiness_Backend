from rest_framework import serializers
from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name','description','category','brand','sku','country_of_origin']

# class ProductVideoSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = ['name','description','category','brand','sku','country_of_origin']

# Serielizer for getting full details 
class ProductFullDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product    
        fields = ['image', 'demo_video']


class ProductDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product 
        fields = ['dimensions', 'color', 'material', 'style_design', 'surface_finish', 'edge_type']


class ProductPricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product       
        fields = ['price', 'offer', 'special_price']

class BulkPricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['bulk_quantity_pricing', 'min_order_quantity','bulk_discount']


class ProductTaxInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['tax_rate', 'tax_code', 'tax_exempt']


class ProductInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product 
        fields = ['stock_quantity', 'availability','inventory_management']


class ProductVariantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['size_variant', 'color_variant', 'style_variant']

class AdditionalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['application_details','maintainance_details','privacy_policy']


class ProductSeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_url','meta_title','meta_description','targeted_keywords','long_tail_keywords']



