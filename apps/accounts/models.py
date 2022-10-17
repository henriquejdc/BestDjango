from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings


# Create your models here.
class UserProfile(models.Model):
    photo = models.ImageField(_('Photo'), upload_to='photos')
    cell_phone = models.CharField(_('Cell Phone'), max_length=16)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    active_language = models.CharField(
        max_length=10,
        choices=settings.LANGUAGES,
        default=settings.LANGUAGE_CODE,
        verbose_name=_("Active Language")
    )

    def __str__(self):
        return '{} - {}'.format(self.user.username, self.cell_phone)

    def clean(self):
        model = self.__class__
        if model.objects.count() > 0 and self.id != model.objects.get().id:
            raise ValidationError(_("Registered profile already exists."))

    class Meta:
        verbose_name = _('User Profile')
        verbose_name_plural = _('User Profiles')
