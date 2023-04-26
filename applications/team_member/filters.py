from django_filters import rest_framework as filters
from .models import Member


class MemeberFilter(filters.FilterSet):
    class Meta:
        model = Member
        fields = ('job_category', )