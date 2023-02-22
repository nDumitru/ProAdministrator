from django import forms
from django.forms import TextInput, NumberInput, EmailInput, Textarea, DateInput, Select

from residents.models import Resident


class ResidentForm(forms.ModelForm):
    class Meta:
        model = Resident
        #  fields = '__all__'
        fields = ['first_name', 'last_name', 'age', 'chirias', 'email', 'management', 'gender',
                  'description', 'start_date', 'end_date']

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your first name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your last name'}),
            'age': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your age'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your email'}),
            'management': Select(attrs={'class': 'form-select'}),
            'gender': Select(attrs={'class': 'form-select'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Please enter your description'}),
            'start_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def clean(self):
        cleaned_data = self.cleaned_data
        get_email = cleaned_data.get('email')  # cleaned_data['email']
        all_students = Resident.objects.all()
        for student in all_students:
            if get_email == student.email:
                msg = f'This email {get_email} exists already in the databases.'
                self._errors['email'] = self.error_class([msg])

        get_start_date = cleaned_data.get('start_date')
        get_end_date = cleaned_data.get('end_date')
        if get_end_date < get_start_date:
            msg = f'The end date is smaller than {get_end_date}  than the start date {get_start_date}.'
            self._errors['end_date'] = self.error_class([msg])

        return cleaned_data


class ResidentUpdateForm(forms.ModelForm):
    class Meta:
        model = Resident
        #  fields = '__all__'
        fields = ['first_name', 'last_name', 'age', 'chirias', 'email', 'management', 'gender',
                  'description', 'start_date', 'end_date']

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your first name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your last name'}),
            'age': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your age'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your email'}),
            'management': Select(attrs={'class': 'form-select'}),
            'gender': Select(attrs={'class': 'form-select'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Please enter your description'}),
            'start_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
