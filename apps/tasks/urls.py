from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    # Categories
    path('category/list', views.list_categories, name='list_category'),
    path('category/add', views.add_category, name='add_category'),
    path('category/edit/<int:id_category>/', views.edit_category, name='edit_category'),
    path('category/delete/<int:id_category>/', views.delete_category, name='delete_category'),
    # Tasks
    path('task/list', views.list_tasks, name='list_task'),
    path('task/add', views.add_task, name='add_task'),
    path('task/edit/<int:id_task>/', views.edit_task, name='edit_task'),
    path('task/delete/<int:id_task>/', views.delete_task, name='delete_task'),
]
