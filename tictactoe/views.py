""" controller logic for the default app """
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def welcome(request):
    """ show a welcome page """
    if request.user.is_authenticated:
        return redirect('player_home')
    else:
        return render(request, "tictactoe/welcome.html")
