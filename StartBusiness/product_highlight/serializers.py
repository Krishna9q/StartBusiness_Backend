from rest_framework import serializers

from product_highlight.models import ProductHighlight
class ProductHighlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductHighlight
        fields = '__all__'