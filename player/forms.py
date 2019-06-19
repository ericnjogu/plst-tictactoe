""" app 'player' forms """
from django.forms import ModelForm
from .models import Invitation

class InvitationForm(ModelForm):
    """ show a form with fields from the 'Invitation' model """
    class Meta:
        model = Invitation
        # pylint complains about exclude
        # exclude = ('from_user', 'timestamp')
        fields = ('to_user', 'message')
