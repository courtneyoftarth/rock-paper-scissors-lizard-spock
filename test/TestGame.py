import unittest
from data.game import Game

class TestGame(unittest.TestCase):
    def test_get_all_moves(self):
        game = Game()
        self.assertEqual(len(game.getAllMoves()), 5)

    def test_get_random_move(self):
        game = Game()
        move = game.getRandomMove()
        self.assertIsNotNone(move)
        self.assertIsNotNone(move.getId())
   
    def test_get_move(self):
        game = Game()
        for i in range(5):
            move = game.getAllMoves()[i]
            self.assertEqual(game.getMove(move.getId()), move)