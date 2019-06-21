""" app 'gameplay' urls """
from django.urls import re_path, path
from .views import game_detail, make_move, AllGames

urlpatterns = [
    re_path(r'detail/(?P<game_id>\d+)', game_detail, name='game_detail'),
    re_path(r'make_move/(?P<game_id>\d+)', make_move, name='game_make_move'),
    path('all/', AllGames.as_view(), name='all_games')
]
