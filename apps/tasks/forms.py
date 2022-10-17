from django import forms

from .models import Task, Category


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        exclude = ('owner',)


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        exclude = ('owner',)
