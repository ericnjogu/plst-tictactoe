""" app 'gameplay' urls """
from django.urls import re_path
from .views import game_detail

urlpatterns = [
    re_path(r'detail/(?P<game_id>\d+)', game_detail, name='game_detail')
]
