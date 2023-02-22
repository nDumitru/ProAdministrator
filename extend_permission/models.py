from django.contrib.auth.models import Permission
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User


class ExtendUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='extend_user')
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.user.username


class ExtendPermission(models.Model):
    extenduser = models.ForeignKey(ExtendUser, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.extenduser.user.username} - {self.permission.name}'

    @staticmethod
    def add_permission_to_extenduser(permission, extenduser):
        # Verifica dacă permisiunea există deja pentru utilizatorul extins
        content_type = ContentType.objects.get_for_model(extenduser)
        existing_permission = Permission.objects.filter(
            content_type=content_type,
            codename=permission.codename,
            name=permission.name,
        ).first()

        if not existing_permission:
            # Dacă permisiunea nu există, o creează
            existing_permission = Permission.objects.create(
                content_type=content_type,
                codename=permission.codename,
                name=permission.name,
            )

        # Asociem permisiunea la utilizatorul extins
        ExtendPermission.objects.create(
            extenduser=extenduser,
            permission=existing_permission,
        )
