import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    type = django_filters.CharFilter(lookup_expr="exact")
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr="lte")
    name = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Product
        fields = "__all__"