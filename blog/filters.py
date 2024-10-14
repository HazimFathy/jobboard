from .models import blog
import django_filters


class blogfilter(django_filters.filterset):
    class Meta:
        model=blog
        fields='__all__'
        exclude=['owner',]