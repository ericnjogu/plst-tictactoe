from django.test import TestCase
from .models import Game
from django.test import TestCase

class GameTest(TestCase):
    def setUp(self):
        self.game = Game()

    def test_new_move_is_not_null(self):
        new_move = self.game.new_move()
        self.assertNotEqual(new_move, None)

    def test_can_get_new_move_for_first_player(self):
        self.game.status = 'F'
        new_move = self.game.new_move()

    def test_can_get_new_move_for_second_player(self):
        self.game.status = 'S'
        new_move = self.game.new_move()

    def test_cannot_get_new_move_when_not_playing(self):
        self.game.status = 'N'
        self.assertRaises(ValueError, self.game.new_move)

# Create your tests here.
