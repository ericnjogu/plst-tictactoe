""" controller logic for app 'gameplay' """
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from gameplay.models import Game
from gameplay.forms import MoveForm

# Create your views here.
@login_required
def game_detail(request, game_id):
    """ show game detail """
    game = get_object_or_404(Game, pk=game_id)
    context = {'game':game}
    if game.is_users_move(request.user):
        context['form'] = MoveForm()
    return render(request, 'gameplay/game_detail.html', context)
    