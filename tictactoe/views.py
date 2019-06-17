""" controller logic for the default app """
from django.shortcuts import render

def welcome(request):
    """ show a welcome page """
    return render(request, "tictactoe/welcome.html")
