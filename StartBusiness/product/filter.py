from django_filters import FilterSet
import django_filters
from product.models import Product

class ProductFilter(FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    class Meta:
        model = Product
        fields = ['name','status']

class ProductHighlightFilter(django_filters.FilterSet):
    hot_deals = django_filters.BooleanFilter(field_name='producthighlight__hot_deals')
    offer = django_filters.BooleanFilter(field_name='producthighlight__offer')
    trending = django_filters.BooleanFilter(field_name='producthighlight__trending')

    class Meta:
        model = Product
        fields = ['hot_deals','offer','trending']