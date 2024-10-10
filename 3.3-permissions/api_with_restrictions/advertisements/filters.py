from django_filters import rest_framework as filters, DateFromToRangeFilter

from .models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры
    create = DateFromToRangeFilter(field_name='created_at')
    update = DateFromToRangeFilter(field_name='updated_at')

    class Meta:
        model = Advertisement
        fields = ['create', 'update']
