from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm, PasswordResetForm, \
    SetPasswordForm
from django.forms import TextInput, EmailInput

from accounts.models import ProAdminUser


class AuthenticationNewForm(AuthenticationForm):
    """Custom authentication form using email instead of username."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Since ProAdminUser uses email as username field, use 'email' instead of 'username'
        self.fields['username'].widget.attrs.update({
            'class': 'form-control form-control-lg',
            'placeholder': 'Introduceți email-ul',
            'autocomplete': 'email'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control form-control-lg',
            'placeholder': 'Introduceți parola',
            'autocomplete': 'current-password'
        })

    def clean_username(self):
        username = self.cleaned_data.get('username', '')
        return username.lower()


class PasswordChangeViewForm(PasswordChangeForm):
    """Custom password change form with larger inputs."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({
            'class': 'form-control form-control-lg',
            'placeholder': 'Introduceți parola veche'
        })
        self.fields['new_password1'].widget.attrs.update({
            'class': 'form-control form-control-lg',
            'placeholder': 'Introduceți parola nouă'
        })
        self.fields['new_password2'].widget.attrs.update({
            'class': 'form-control form-control-lg',
            'placeholder': 'Confirmați parola nouă'
        })


class PasswordResetViewForm(PasswordResetForm):
    """Custom password reset form."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'class': 'form-control form-control-lg',
            'placeholder': 'Introduceți email-ul'
        })


class PasswordResetConfirmView(SetPasswordForm):
    """Custom password reset confirm form."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_password1'].widget.attrs.update({
            'class': 'form-control form-control-lg',
            'placeholder': 'Introduceți parola nouă'
        })
        self.fields['new_password2'].widget.attrs.update({
            'class': 'form-control form-control-lg',
            'placeholder': 'Confirmați parola nouă'
        })


class UserExtendForm(UserCreationForm):
    """User registration form for ProAdminUser."""

    class Meta:
        model = ProAdminUser
        fields = ['first_name', 'last_name', 'email']

        widgets = {
            'first_name': TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Introduceți prenumele'
            }),
            'last_name': TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Introduceți numele'
            }),
            'email': EmailInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Introduceți email-ul'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control form-control-lg',
            'placeholder': 'Introduceți parola'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control form-control-lg',
            'placeholder': 'Confirmați parola'
        })