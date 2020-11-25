from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='user'),
    path('<int:id>/', views.show, name='show'),
    path('login/', views.auth, name='login'),
]
