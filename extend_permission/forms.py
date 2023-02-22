from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from models import ExtendPermission, Permission


class ExtendUserForm(forms.ModelForm):
    permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label=_("Permissions"),
        required=False,
    )

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "permissions"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields["permissions"].initial = self.instance.user_permissions.all()

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            if self.cleaned_data["permissions"]:
                extended_permission = ExtendPermission.objects.get_or_create(user=user)[0]
                extended_permission.permissions.set(self.cleaned_data["permissions"])
        return user


class ExtendPermissionForm(forms.Form):
    """
    Form used to grant or revoke user permissions.
    """
    user = forms.ModelChoiceField(queryset=User.objects.all())
    permission = forms.ChoiceField(choices=[('view', 'View'), ('change', 'Change')], widget=forms.RadioSelect)
    app_label = forms.CharField()
    model_name = forms.CharField()
