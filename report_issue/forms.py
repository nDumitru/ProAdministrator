from django import forms
from .models import ReportedIssue


class ReportIssueForm(forms.ModelForm):
    """Form for reporting building issues."""

    class Meta:
        model = ReportedIssue
        fields = ['resident_name', 'apartment_number', 'issue_type', 'description']
        widgets = {
            'resident_name': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Introduceți numele dumneavoastră'
            }),
            'apartment_number': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Ex: 101, A2'
            }),
            'issue_type': forms.Select(attrs={
                'class': 'form-select form-select-lg'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Descrieți problema în detaliu...',
                'rows': 5
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['resident_name'].label = 'Nume Rezident'
        self.fields['apartment_number'].label = 'Număr Apartament'
        self.fields['issue_type'].label = 'Tip Problemă'
        self.fields['description'].label = 'Descriere'
