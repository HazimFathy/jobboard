import django_filters
from .models import job



class jobFilter(django_filters.FilterSet):
    description= django_filters.CharFilter(lookup_expr='icontains')
    title= django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = job
        fields = '__all__'
        exclude=['Published_on','image','slug','owner',]