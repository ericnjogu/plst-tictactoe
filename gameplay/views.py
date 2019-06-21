""" controller logic for app 'gameplay' """
from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import PermissionDenied
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

@login_required
def make_move(request, game_id):
    """ persist the move if available """
    game = get_object_or_404(Game, pk=game_id)
    if not game.is_users_move(request.user):
        raise PermissionDenied
    move = game.new_move()
    form = MoveForm(instance=move, data=request.POST)
    if form.is_valid:
        form.save()
        return redirect(game)
    else:
        return render(request, 'gameplay/game_detail.html', {'game':game, 'form':form})
    