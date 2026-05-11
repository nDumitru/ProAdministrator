from django import forms
from django.utils.translation import gettext_lazy as _

from extend_permission.models import ExtendPermission, ExtendUser
from django.contrib.auth.models import Permission


class ExtendUserForm(forms.ModelForm):
    permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label=_("Permissions"),
        required=False,
    )

    class Meta:
        model = ExtendUser
        fields = ["phone", "permissions"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields["permissions"].initial = self.instance.extendpermission_set.values_list('permission', flat=True)

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            if self.cleaned_data.get("permissions"):
                # Clear existing permissions and set new ones
                self.instance.extendpermission_set.all().delete()
                for perm in self.cleaned_data["permissions"]:
                    ExtendPermission.objects.create(
                        extenduser=self.instance,
                        permission=perm
                    )
        return user


class ExtendPermissionForm(forms.Form):
    """
    Form used to grant or revoke user permissions.
    """
    user = forms.ModelChoiceField(queryset=ExtendUser.objects.all())
    permission = forms.ChoiceField(
        choices=[
            ('view', 'View'),
            ('change', 'Change'),
            ('add', 'Add'),
            ('delete', 'Delete'),
        ],
        widget=forms.RadioSelect,
        label=_("Permission Type")
    )
    app_label = forms.CharField(label=_("App Label"))
    model_name = forms.CharField(label=_("Model Name"))
