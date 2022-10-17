# DJANGO IMPORTS
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

# PROJECT IMPORTS
from .form import UserForm, UserProfileForm, ChangeUserForm
from .models import UserProfile


def add_user(request):
    template_name = 'accounts/add_user.html'
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.set_password(f.password)
            f.save()
            messages.success(request, _('Saved successfully!'))
            return redirect('core:home')
        messages.error(request, form.errors)
    context = {'form': form}
    return render(request, template_name, context)


def login_user(request):
    template_name = 'accounts/login_user.html'

    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(request.GET.get('next', '/'))
        else:
            messages.error(request, _('Username or Password incorrect!'))

    return render(request, template_name, {})


@login_required(login_url='/accounts/login-user')
def logout_user(request):
    logout(request)
    return redirect('accounts:login_user')


@login_required(login_url='/accounts/login-user')
def change_password_user(request):
    template_name = 'accounts/change_password_user.html'
    form = PasswordChangeForm(user=request.user)

    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, _('Change password successfully!'))
        else:
            messages.error(request, _('Not possible change password!'))
            messages.error(request, form.errors)

    context = {'form': form}
    return render(request, template_name, context)


@login_required(login_url='/accounts/login-user')
def list_profile_user(request):
    template_name = 'accounts/list_profile_user.html'
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        profile = None
    context = {'profile': profile}
    return render(request, template_name, context)


@login_required(login_url='/accounts/login-user')
def profile_user(request, username: str = None):
    """
        View to add and change userprofile if username exists
    """
    template_name = 'accounts/add_profile_user.html'
    form = UserProfileForm()
    user = None
    if username:
        try:
            user = UserProfile.objects.get(user__username=username)
            form = UserProfileForm(instance=user)
        except UserProfile.DoesNotExist:
            try:
                user = UserProfile.objects.get(user=request.user)
                form = UserProfileForm(instance=user)
            except UserProfile.DoesNotExist:
                pass

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user)

        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            update_session_auth_hash(request, f.user)
            messages.success(request, _('Profile Updated successfully!'))
        else:
            messages.error(request, _('Not possible Updated profile!'))
            messages.error(request, form.errors)

    context = {'form': form}
    return render(request, template_name, context)


@login_required(login_url='/accounts/login-user')
def change_user(request, username: str = None):
    template_name = 'accounts/change_user.html'
    try:
        user = User.objects.get(username=username)
        form = ChangeUserForm(instance=user)
    except UserProfile.DoesNotExist:
        user = request.user
        form = ChangeUserForm(instance=user)

    if request.method == 'POST':
        form = ChangeUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, _('Updated successfully!'))
            return redirect('core:home')
        messages.error(request, form.errors)
    context = {'form': form}
    return render(request, template_name, context)
