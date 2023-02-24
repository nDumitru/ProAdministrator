from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
from .models import Resident


class ResidentForm(forms.ModelForm):
    class Meta:
        model = Resident
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'date_of_birth',
            'apartment',
            'start_date',
            'end_date',
            'notes',
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['phone_number'].validators.append(MinValueValidator(1000000000))
        self.fields['phone_number'].validators.append(MaxValueValidator(9999999999))

    def clean_first_name(self):
        return self.cleaned_data['first_name'].capitalize()

    def clean_last_name(self):
        return self.cleaned_data['last_name'].capitalize()


class ResidentUpdateForm(forms.ModelForm):
    class Meta:
        model = Resident
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'apartment']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'phone_number': 'Phone Number',
            'apartment': 'Apartment'
        }

    def clean_first_name(self):
        return self.cleaned_data['first_name'].capitalize()

    def clean_last_name(self):
        return self.cleaned_data['last_name'].capitalize()
