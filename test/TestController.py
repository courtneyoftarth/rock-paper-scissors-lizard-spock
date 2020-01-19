import unittest
import json
from controller import app

class TestController(unittest.TestCase):
    def test_get_choices(self):
        response = app.test_client().get('/choices')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, '[{"id":1,"name":"rock"},{"id":2,"name":"paper"},{"id":3,"name":"scissors"},{"id":4,"name":"lizard"},{"id":5,"name":"spock"}]\n')

    def test_get_choice(self):
        response = app.test_client().get('/choice')
        self.assertEqual(response.status_code, 200)
        self.assertRegexpMatches(response.data, r'{"id":[\d]+,"name":"[a-z]+"}')

    def test_play_throws_400_when_move_is_missing(self):
        response = app.test_client().post('/play')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Expected parameter player', response.data)

    def test_play_throws_400_when_move_is_invalid(self):
        response = app.test_client().post('/play', data=json.dumps({
            "player": 3823
        }), content_type="application/json")
        self.assertEqual(response.status_code, 400)
        self.assertIn('Parameter player is not a valid move id', response.data)
    
    def test_play_returns_correct_result(self):
        response = app.test_client().post('/play', data=json.dumps({
            "player": 1
        }), content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertRegexpMatches(response.data, r'{"computer":[0-9]+,"player":[0-9]+,"results":"[a-z]+"}\n')
