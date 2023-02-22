import django_filters
from django import forms
from django_filters import DateFilter

from residents.models import Resident
from management.models import Administrator


# lookup_expr -> icontains,startswith, endswith, lt, lte, gt, gte

# lt - less than
# lte - less than, or equal to

# gt - greater than
# gte - greater then, or equal to


class ResidentFilter(django_filters.FilterSet):

    first_name = django_filters.CharFilter(lookup_expr='icontains', label='First name')
    last_name = django_filters.CharFilter(lookup_expr='icontains', label='Last name')

    start_date_gte = DateFilter(field_name='start_date', lookup_expr='gte', label='From start date',
                                widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))

    start_date_lte = DateFilter(field_name='start_date', lookup_expr='lte', label='To start date',
                                widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))

    end_date_gte = DateFilter(field_name='end_date', lookup_expr='gte', label='From end date',
                              widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))

    end_date_lte = DateFilter(field_name='end_date', lookup_expr='lte', label='To end date',
                              widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))

    class Meta:
        model = Resident
        fields = ['first_name', 'last_name', 'is_olympic', 'start_date_gte', 'start_date_lte',  'end_date_gte',
                  'end_date_lte', 'management']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['first_name'].field.widget.attrs.update({'class': 'form-control', 'placeholder':
                                                              'Plase enter first name'})
        self.filters['last_name'].field.widget.attrs.update({'class': 'form-control', 'placeholder':
                                                             'Plase enter last name'})
        self.filters['is_olympic'].field.widget.attrs.update({'class': 'form-select'})
        self.filters['management'].field.widget.attrs.update({'class': 'form-select'})
        self.filters['management'].field.queryset = Administrator.objects.filter(active=True)
