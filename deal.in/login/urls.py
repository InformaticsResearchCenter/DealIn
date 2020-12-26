from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('show/<slug:id>/', views.show, name='show'),
    path('login/', views.auth, name='login'),
]
