from django_filters import FilterSet
from product_highlight.models import ProductHighlight


class ProductHighlightFilter(FilterSet):
    
    class Meta:
        model = ProductHighlight
        fields = ['hot_deals','trending']