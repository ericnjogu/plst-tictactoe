""" app 'player' models """
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Invitation(models.Model):
    """ an invitation to play a tictactoe game """
    from_user = models.ForeignKey(User, related_name='invitations_sent', on_delete=models.CASCADE)
    to_user = models.ForeignKey(
        User,
        related_name='invitations_received',
        on_delete=models.CASCADE,
        verbose_name="User to invite",
        help_text="select from list")
    message = models.CharField(
        max_length=300,
        verbose_name='optional message',
        help_text='personal invitation',
        blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
