from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Category(models.Model):
    name = models.CharField(_('Name'), max_length=150)
    description = models.TextField(_('Description'), blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ['id']

    def __str__(self):
        return '{} - {}'.format(self.id, self.name)


class Task(models.Model):
    PRIORITY_CHOICES = (
        ('L', _('LOW')),
        ('M', _('MEDIUM')),
        ('H', _('HIGH')),
    )
    STATUS_CHOICES = (
        ('I', _('IN PROGRESS')),
        ('P', _('PENDING')),
        ('C', _('COMPLETED')),
    )
    name = models.CharField(_('Name'), max_length=200)
    description = models.TextField(_('Description'))
    end_date = models.DateField(_('End Date'), auto_now=False, auto_now_add=False)
    priority = models.CharField(_('Priority'), max_length=1, choices=PRIORITY_CHOICES)
    category = models.ManyToManyField(Category)
    status = models.CharField(_('Status'), max_length=1, choices=STATUS_CHOICES)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Task')
        verbose_name_plural = _('Tasks')
        ordering = ['id']

    def __str__(self):
        return '{} - {}'.format(self.id, self.name)

    def list_categories(self):
        return ', '.join([cat.name for cat in self.category.all()])
    list_categories.short_description = _("Categories")
