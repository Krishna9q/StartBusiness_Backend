from django_filters import FilterSet
import django_filters
from product.models import Product

class ProductFilter(FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    category_ids = django_filters.CharFilter(method='filter_by_category_ids')
    class Meta:
        model = Product
        fields = ['name','status','brand','category_ids']



def filter_by_category_ids(self, queryset,value):
        category_ids = value.split(',') 
        return queryset.filter(categories__id__in=category_ids).distinct()

