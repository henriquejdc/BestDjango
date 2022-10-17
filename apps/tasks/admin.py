from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from apps.tasks.models import Category, Task


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'owner']
    search_fields = ['name', 'description']
    list_filter = ['name', 'owner']


def mark_all_tasks_done(modeladmin, request, queryset):
    queryset.update(status='C')


mark_all_tasks_done.short_description = _('Mark tasks as complete.')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'end_date', 'priority',  'list_categories', 'status']
    search_fields = ['name', 'description']
    list_filter = ['priority', 'owner', 'category']
    actions = [mark_all_tasks_done]

    # def list_categories(self, obj: Task):
    #     return ', '.join([cat.name for cat in obj.category.all()])
    # list_categories.short_description = _("Categories")


admin.site.register(Category, CategoryAdmin)
# admin.site.register(Task, TaskAdmin)
