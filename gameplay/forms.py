""" app 'gameplay' forms """
from django.forms import ModelForm
from .models import Move

class MoveForm(ModelForm):
    """ allow user to make a move """
    class Meta:
        model = Move
        fields = ['x', 'y', 'comments']
        