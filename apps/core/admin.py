from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.utils.translation import gettext_lazy as _

# Register your models here.

# admin.site.unregister(User)
# admin.site.unregister(Group)

admin.site.site_header = _('DjangoBest Login')
admin.site.site_title = _('DjangoBest Admin')
admin.site.index_title = _('DjangoBest Admin - Application')
