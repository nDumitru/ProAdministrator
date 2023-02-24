from django import forms
from django.forms import TextInput, NumberInput, EmailInput, Textarea, DateInput

from management.models import Administrator


class AdministratorForm(forms.ModelForm):
    class Meta:
        model = Administrator
        fields = ['first_name', 'last_name', 'course',
                  'description', 'start_date', 'end_date']

        widgets ={
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your first name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your last name'}),
            'course': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your course'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Please enter your description'}),
            'start_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def __init__(self, show_all_fields, *args, **kwargs):
        super().__init__(*args, **kwargs)
        exclude = ['start_date', 'end_date']
        if show_all_fields is False:
            for item in exclude:
                self.fields.pop(item)

class AdministratorUpdateForm(forms.ModelForm):
    class Meta:
        model = Administrator

        fields = ['first_name', 'last_name', 'course',
                  'description', 'start_date', 'end_date']

        widgets ={
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your first name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your last name'}),
            'course': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your course'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Please enter your description'}),
            'start_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }