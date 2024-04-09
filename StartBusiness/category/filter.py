from django_filters import FilterSet
from category.models import Category

class CategoryFilter(FilterSet):
    class Meta:
        model = Category
        fields = ['is_active']