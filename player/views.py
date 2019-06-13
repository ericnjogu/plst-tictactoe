"""controller logic for player app"""
from django.shortcuts import render
from gameplay.models import Game
# Create your views here.

def home(request):
    """respond to /home requests"""
    return render(request, "player/home.html",
        {'ngames': Game.objects.count()})