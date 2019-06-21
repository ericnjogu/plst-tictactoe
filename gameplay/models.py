""" app 'gameplay' models"""
from django.db import models
from django.db.models import QuerySet, Q
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

GAME_STATUS_CHOICES = (
    ('F', 'First player to move'),
    ('S', 'Second player to move'),
    ('W', 'First player wins'),
    ('L', 'Second player wins'),
    ('D', 'Draw')
)

BOARD_SIZE = 3

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

    def get_absolute_url(self):
        """ generate URL to this game instance """
        return reverse('game_detail', args=[self.id])

    def __str__(self):
        return "{0} vs {1}".format(self.first_player, self.second_player)

    def board(self):
        """ return 2D list of 'Move' objects """
        board = [[None for x in range(BOARD_SIZE)] for y in range(BOARD_SIZE)]
        for move in self.move_set.all():
            board[move.x][move.y] = move
        return board

    def is_users_move(self, user):
        """ true if the provided user is meant to make a move """
        return (user == self.first_player and self.status == 'F') or\
                (user == self.second_player and self.status == 'S')

    def new_move(self):
        """ returns new move """
        if self.status not in 'FS':
            raise ValueError('cannot make move on finished game')
        return Move(
            game=self,
            by_first_player=self.status == 'F'
            )

class Move(models.Model):
    """a tictactoe game move"""
    x = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(BOARD_SIZE - 1)]
    )
    y = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(BOARD_SIZE - 1)]
    )
    comments = models.CharField(max_length=300, blank=True)
    by_first_player = models.BooleanField(editable=False)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, editable=False)
