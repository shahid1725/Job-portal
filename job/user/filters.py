from django.contrib.auth.models import User
import django_filters
from home.models import Job
from django_filters.filters import RangeFilter



class SearchFilter(django_filters.FilterSet):
    title=django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Job
        fields=['title']

