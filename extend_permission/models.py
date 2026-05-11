from django.contrib.auth.models import Permission
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.conf import settings


class ExtendUser(models.Model):
    """Extended user profile with additional fields."""
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='extend_user')
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return str(self.user.email)


class ExtendPermission(models.Model):
    """Custom permission extension for users."""
    extenduser = models.ForeignKey(ExtendUser, on_delete=models.CASCADE, related_name='permissions')
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.extenduser} - {self.permission.name}'

    @staticmethod
    def add_permission_to_extenduser(permission, extenduser):
        """Add a permission to an extended user."""
        # Check if permission already exists for the extended user
        content_type = ContentType.objects.get_for_model(extenduser)
        existing_permission = Permission.objects.filter(
            content_type=content_type,
            codename=permission.codename,
            name=permission.name,
        ).first()

        if not existing_permission:
            # If permission doesn't exist, create it
            existing_permission = Permission.objects.create(
                content_type=content_type,
                codename=permission.codename,
                name=permission.name,
            )

        # Associate the permission with the extended user
        ExtendPermission.objects.create(
            extenduser=extenduser,
            permission=existing_permission,
        )