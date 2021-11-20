from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),

    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),

    path('logout/', auth_views.logout_then_login, name='logout_then_login'),
    path('profile/', views.profile, name='profile'),
    
    path('password_change/', auth_views.PasswordChangeView, name='PasswordChangeView'),
    path('password_reset/', views.password_reset_request, name='password_reset'),

    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),

]