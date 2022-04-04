from django.urls import path
from .views import *

urlpatterns = [
    path('register', RegisterView.as_view(), name='Register'),
    path('login', LoginView.as_view(), name='Login'),
    path('user', UserView.as_view(), name='User'),
    path('logout', LogoutView.as_view(), name='Logout'),
]