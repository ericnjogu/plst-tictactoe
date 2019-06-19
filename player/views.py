"""controller logic for player app"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from gameplay.models import Game
from .forms import InvitationForm

# Create your views here.

def home(request):
    """respond to /home requests"""

    all_my_games = Game.objects.games_for_user(request.user)
    active_games = all_my_games.active()

    return render(request, "player/home.html",
                  {'games': active_games})

@login_required
def new_invitation(request):
    """ show an a invitation form """
    form = InvitationForm()
    return render(request, "player/new_invitation_form.html", {'form': form})
    