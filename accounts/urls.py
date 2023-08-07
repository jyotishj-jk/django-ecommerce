from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'), #For login page
    path('register/', views.register, name='register'), #For register page
    path('logout', views.logout, name='logout'), #For logout page
    path('dashboard/', views.dashboard, name='dashboard') #For dashboard page
]