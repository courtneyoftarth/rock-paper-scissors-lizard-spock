from unittest import TestCase
from unittest.mock import MagicMock
import json
from controller import app, game
from model.move import Move

class TestController(TestCase):
    def setUp(self):
        game.getRandomMove = MagicMock(return_value=Move('test-move'))

    def test_get_choices(self):
        response = app.test_client().get('/choices')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 5)

    def test_get_choice(self):
        response = app.test_client().get('/choice')
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json['id'])
        self.assertIsNotNone(response.json['name'])

    def test_play_throws_400_when_move_is_missing(self):
        response = app.test_client().post('/play')
        self.assertEqual(response.status_code, 400)

    def test_play_throws_400_when_move_is_invalid(self):
        response = app.test_client().post('/play', data=json.dumps({
            "player": 3823
        }), content_type="application/json")
        self.assertEqual(response.status_code, 400)
    
    def test_play_returns_correct_result(self):
        response = app.test_client().post('/play', data=json.dumps({
            "player": 1
        }), content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json['computer'])
        self.assertIsNotNone(response.json['player'])
        self.assertIsNotNone(response.json['results'])
