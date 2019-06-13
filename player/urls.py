""" url patterns"""
from django.conf.urls import re_path
from .views import home

urlpatterns = [
    re_path('home$', home)
]