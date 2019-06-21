""" url patterns"""
from django.urls import re_path, path
from django.contrib.auth.views import LoginView, LogoutView

from .views import home, new_invitation, accept_invitation, SignupView

urlpatterns = [
    re_path('home$', home, name='player_home'),
    re_path('login$',
            LoginView.as_view(template_name='player/login_form.html'),
            name='player_login'),
    re_path('logout$',
            LogoutView.as_view(),
            name='player_logout'),
    re_path('invite$', new_invitation, name='new_player_invitation'),
    re_path(r'accept_invitation/(?P<invite_id>\d+)$',
            accept_invitation,
            name='accept_game_invitation'),
    path('signup', SignupView.as_view(), name='player_signup')
]
