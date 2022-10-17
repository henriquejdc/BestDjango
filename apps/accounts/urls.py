from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('add-user/', views.add_user, name='add_user'),
    path('change-user/<str:username>/', views.change_user, name='change_user'),
    path('change-user/', views.change_user, name='change_user'),
    path('login-user/', views.login_user, name='login_user'),
    path('logout-user/', views.logout_user, name='logout_user'),
    path('change-password-user/', views.change_password_user, name='change_password_user'),
    path('profile-user/<str:username>/', views.profile_user, name='profile_user'),
    path('profile-user/', views.profile_user, name='profile_user'),
    path('my-profile-user/', views.list_profile_user, name='list_profile_user'),
]
