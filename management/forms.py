from django import forms
from django.forms import TextInput, Textarea, DateInput
from management.models import Administrator
from .models import Block, Apartment, Resident, Manager


class BlockForm(forms.ModelForm):
    class Meta:
        model = Block
        fields = '__all__'


class ApartmentForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = '__all__'


class ResidentForm(forms.ModelForm):
    class Meta:
        model = Resident
        fields = '__all__'


class ManagerForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = '__all__'


class AdministratorForm(forms.ModelForm):
    class Meta:
        model = Administrator
        fields = ['first_name', 'last_name', 'bloc',
                  'description', 'start_date', 'end_date']

    widgets = {
        'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your first name'}),
        'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your last name'}),
        'bloc': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your bloc number'}),
        'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Please enter your description'}),
        'start_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        'end_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
    }

    def __init__(self, show_all_fields, *args, **kwargs):
        super().__init__(*args, **kwargs)
        exclude = ['start_date', 'end_date']
        if not show_all_fields:
            for item in exclude:
                self.fields.pop(item)


class AdministratorUpdateForm(forms.ModelForm):
    class Meta:
        model = Administrator
        fields = ['first_name', 'last_name', 'bloc', 'description', 'start_date', 'end_date']
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your first name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your last name'}),
            'bloc': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your bloc number'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Please enter your description'}),
            'start_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
