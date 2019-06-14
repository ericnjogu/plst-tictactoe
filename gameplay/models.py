""" app 'gameplay' models"""
from django.db import models
from django.db.models import QuerySet, Q
from django.contrib.auth.models import User

GAME_STATUS_CHOICES = (
    ('F', 'First player to move'),
    ('S', 'Second player to move'),
    ('W', 'First player wins'),
    ('L', 'Second player wins'),
    ('D', 'Draw')
)

class GameQuerySet(QuerySet):
    """DAO for Games, accessible via Game.objects"""
    def games_for_user(self, user):
        """all games where the user is first or second player"""
        return self.filter(Q(first_player=user) | Q(second_player=user))

    def active(self):
        """all active games"""
        return self.filter(Q(status='F') | Q(status='S'))

class Game(models.Model):
    """a tictactoe Game"""
    first_player = models.ForeignKey(User, related_name='games_first_player',
                                     on_delete=models.CASCADE)
    second_player = models.ForeignKey(User, related_name='games_second_player',
                                      on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, default='F', choices=GAME_STATUS_CHOICES)

    objects = GameQuerySet.as_manager()

    def __str__(self):
        return "{0} vs {1}".format(self.first_player, self.second_player)

class Move(models.Model):
    """a tictactoe game move"""
    x = models.IntegerField()
    y = models.IntegerField()
    comments = models.CharField(max_length=300, blank=True)
    by_first_player = models.BooleanField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
