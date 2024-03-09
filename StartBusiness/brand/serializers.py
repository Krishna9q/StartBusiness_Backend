from rest_framework import serializers
from brand.models import Brand

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class DealerViewAccordingBrand(serializers.ModelSerializer):
    Dealer = serializers.ListField()
    class Meta:
        model = Brand
        fields = ['Dealer']