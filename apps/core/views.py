from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from datetime import datetime

from ..tasks.models import Task


@login_required(login_url='/accounts/login-user')
def home(request) -> render:
    context = {'tasks': Task.objects.filter(
        end_date__lte=datetime.today(),
        owner=request.user
    ).exclude(status='C')}
    return render(request, 'core/home.html', context)


@login_required(login_url='/accounts/login-user')
def search_tasks(request) -> render:
    template_name = 'tasks/list_tasks.html'
    query = request.GET.get('query')
    tasks = Task.objects.filter(
        Q(name__icontains=query),
        Q(description__icontains=query)
    ).filter(owner=request.user)
    context = {'tasks': tasks}
    return render(request, template_name, context)
