import unittest
from model.move import Move

class TestMove(unittest.TestCase):
    def test_id_is_unique(self):
        move1 = Move("test-move-1")
        move2 = Move("test-move-2")
        self.assertNotEqual(move1.getId(), move2.getId())

    def test_get_serialized(self):
        move = Move("test-move")
        self.assertEqual(move.getSerialized(), {
            "id": move.getId(),
            "name": "test-move"
        })

    def test_is_winner_does_not_win_unknown_move(self):
        move = Move("test-move")
        self.assertFalse(move.isWinner(Move("other-move")))

    def test_is_winner_does_not_win_equal_move(self):
        move = Move("test-move")
        self.assertFalse(move.isWinner(move))

    def test_is_winner_wins_only_beatable_move(self):
        paper = Move("paper")
        rock = Move("rock")

        paper.addBeats(rock)

        self.assertTrue(paper.isWinner(rock))

    def test_is_winner_beats_all_beatable_moves(self):
        paper = Move("paper")
        rock = Move("rock")
        spock = Move("spock")

        paper.addBeats(rock, spock)

        self.assertTrue(paper.isWinner(rock))
        self.assertTrue(paper.isWinner(spock))
