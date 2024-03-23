from django_filters import FilterSet
from dealer.models import Dealer
import django_filters


class DealerFilter(FilterSet):
    dealer_name = django_filters.CharFilter(field_name='dealer_name', lookup_expr='icontains')
    class Meta:
        model = Dealer
        fields = ['dealer_name','is_active']