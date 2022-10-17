from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from .forms import CategoryForm, TaskForm
from .models import Category, Task


@login_required(login_url='/accounts/login-user')
def add_category(request) -> render:
    template_name = 'tasks/add_category.html'
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.owner = request.user
            f.save()
            messages.success(request, _('Saved successfully!'))
            return redirect('tasks:list_category')
        messages.error(request, form.errors)

    context = {'form': form}
    return render(request, template_name, context)


@login_required(login_url='/accounts/login-user')
def list_categories(request) -> render:
    template_name = 'tasks/list_categories.html'
    context = {'categories': Category.objects.all()}
    return render(request, template_name, context)


@login_required(login_url='/accounts/login-user')
def edit_category(request, id_category) -> render or redirect:
    template_name = 'tasks/add_category.html'
    category = get_object_or_404(Category, pk=id_category, owner=request.user)
    form = CategoryForm(instance=category)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, _('Saved successfully!'))
            return redirect('tasks:list_category')
        messages.error(request, form.errors)

    context = {'form': form}
    return render(request, template_name, context)


@login_required(login_url='/accounts/login-user')
def delete_category(request, id_category) -> redirect:
    category = get_object_or_404(Category, pk=id_category, owner=request.user)
    category.delete()
    messages.success(request, _('Deleted successfully!'))
    return redirect('tasks:list_category')


@login_required(login_url='/accounts/login-user')
def add_task(request) -> render:
    template_name = 'tasks/add_task.html'
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.owner = request.user
            f.save()
            form.save_m2m()
            messages.success(request, _('Saved successfully!'))
            return redirect('tasks:list_tasks')
        messages.error(request, form.errors)

    context = {'form': form}
    return render(request, template_name, context)


@login_required(login_url='/accounts/login-user')
def list_tasks(request) -> render:
    template_name = 'tasks/list_tasks.html'
    context = {'tasks': Task.objects.filter(owner=request.user).exclude(status='C')}
    return render(request, template_name, context)


@login_required(login_url='/accounts/login-user')
def edit_task(request, id_task) -> render or redirect:
    template_name = 'tasks/add_task.html'
    task = get_object_or_404(Task, pk=id_task, owner=request.user)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        if form.is_valid():
            form = TaskForm(request.POST, instance=task)
            form.save()
            messages.success(request, _('Saved successfully!'))
            return redirect('tasks:list_task')
        messages.error(request, form.errors)

    context = {'form': form}
    return render(request, template_name, context)


@login_required(login_url='/accounts/login-user')
def delete_task(request, id_task) -> redirect:
    task = get_object_or_404(Category, pk=id_task, owner=request.user)
    task.delete()
    messages.success(request, _('Deleted successfully!'))
    return redirect('tasks:list_task')
