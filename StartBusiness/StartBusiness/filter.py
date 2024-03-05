from django_filters import FilterSet

from brand.models import Brand
import django_filters




class BrandFilter(FilterSet):
    brand_name = django_filters.CharFilter(field_name='brand_name', lookup_expr='icontains')
    is_active = django_filters.BooleanFilter(field_name='is_active')
    # category = django_filters.UUIDFilter(field_name='category' )

    class Meta:
        model = Brand
        fields = ['brand_name','category', 'is_active']
        
                
      













