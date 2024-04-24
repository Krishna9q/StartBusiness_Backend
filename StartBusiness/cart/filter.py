from django_filters import FilterSet
import django_filters
from cart.models import Cart

class CartFilter(FilterSet):
    class Meta:
        model = Cart
        fields = ['user']