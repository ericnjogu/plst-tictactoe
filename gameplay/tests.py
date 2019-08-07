from django.test import TestCase
from .models import Game
from django.test import TestCase

class GameTest(TestCase):
    def test_new_move_is_not_null(self):
        game = Game()
        new_move = game.new_move()
        self.assertNotEqual(new_move, None)

# Create your tests here.
