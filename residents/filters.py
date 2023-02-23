import django_filters
from django import template
from residents.models import Resident


class ResidentFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    birth_date = django_filters.DateFilter()
    entry_date = django_filters.DateFilter()
    exit_date = django_filters.DateFilter()

    class Meta:
        model = Resident
        fields = ['first_name', 'last_name', 'birth_date', 'entry_date', 'exit_date']


register = template.Library()


@register.filter(name='addcss')
def addcss(field, css):
    return field.as_widget(attrs={"class": css})
