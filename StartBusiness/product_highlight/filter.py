from django_filters import FilterSet
import django_filters
from product.models import Product


class ProductHighlightFilter(django_filters.FilterSet):
    hot_deals = django_filters.BooleanFilter(field_name='producthighlight__hot_deals')
    offer = django_filters.BooleanFilter(field_name='producthighlight__offer')
    trending = django_filters.BooleanFilter(field_name='producthighlight__trending')
    best_seller = django_filters.BooleanFilter(field_name='producthighlight__best_seller')

    class Meta:
        model = Product
        fields = ['hot_deals','offer','trending','best_seller']