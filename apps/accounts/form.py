from django import forms
from django.contrib.auth.models import User

from .models import UserProfile


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email']


class ChangeUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        exclude = ['user']
