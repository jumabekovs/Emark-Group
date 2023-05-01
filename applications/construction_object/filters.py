from django_filters import rest_framework as filters
from .models import Construction, Flat


class ConstructionFilter(filters.FilterSet):
    start_price = filters.NumberFilter(field_name='cost_per_square_meter', lookup_expr="gte")
    end_price = filters.NumberFilter(field_name='cost_per_square_meter', lookup_expr="lte")

    class Meta:
        model = Construction
        fields = ('type', 'offer', 'district', 'start_price', 'end_price', 'construction_completion_year', 'selling_status')


class FlatFilter(filters.FilterSet):
    start_price = filters.NumberFilter(field_name='price', lookup_expr="gte")
    end_price = filters.NumberFilter(field_name='price', lookup_expr="lte")

    class Meta:
        model = Flat
        fields = ('type', 'rooms', 'start_price', 'end_price', 'block')
