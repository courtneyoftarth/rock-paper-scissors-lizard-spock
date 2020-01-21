from unittest import TestCase
from unittest.mock import MagicMock
from model.game import Game, random

game = Game()

class TestGame(TestCase):
    def setUp(self):
        random.getRandom = MagicMock(return_value=0)

    def test_get_all_moves(self):
        self.assertEqual(len(game.getAllMoves()), 5)

    def test_get_random_move(self):
        move = game.getRandomMove()
        self.assertIsNotNone(move)
        self.assertIsNotNone(move.getId())
   
    def test_get_move(self):
        for i in range(5):
            move = game.getAllMoves()[i]
            self.assertEqual(game.getMove(move.getId()), move)

    def test_has_move_returns_true_when_move_is_valid(self):
        for i in range(5):
            move = game.getAllMoves()[i]
            self.assertTrue(game.hasMove(move.getId()))

    def test_has_move_returns_false_when_move_is_invalid(self):
        self.assertFalse(game.hasMove(1000))