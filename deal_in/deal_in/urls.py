from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('login/', views.login, name='login'),
    path('description/', views.deskripsi, name='desc'),
    path('about/', views.tentang, name='tentang'),
    path('', views.index, name='home'),
    path('user/', include('login.urls')),
]
