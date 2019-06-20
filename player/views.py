"""controller logic for player app"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from gameplay.models import Game
from player.models import Invitation
from .forms import InvitationForm

# Create your views here.

def home(request):
    """respond to /home requests"""

    all_my_games = Game.objects.games_for_user(request.user)
    active_games = all_my_games.active()
    invites_received = request.user.invitations_received.all()

    return render(request, "player/home.html",
                  {'games': active_games,
                   'invites_received':invites_received
                  })

@login_required
def new_invitation(request):
    """ show an a invitation form """
    if request.method == 'POST':
        invite = Invitation(from_user=request.user)
        form = InvitationForm(instance=invite, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('player_home')
    else:
        form = InvitationForm()
    return render(request, "player/new_invitation_form.html", {'form': form})

@login_required
def accept_invitation(request, invite_id):
    """ accept an a invitation """
    invitation = get_object_or_404(Invitation, pk=invite_id)
    if request.user != invitation.to_user:
        raise PermissionDenied

    if request.method == 'POST':
        if 'accept' in request.POST:
            game = Game.objects.create(
                first_player=invitation.to_user,
                second_player=invitation.from_user
            )
        invitation.delete()
        return redirect(game)
    else:
        return render(
            request,
            'player/accept_invitation_form.html',
            {'invitation':invitation}
        )
    