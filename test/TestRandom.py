from unittest import TestCase
from service.random import Random, URL
import requests_mock

class TestRandom(TestCase):
    @requests_mock.Mocker()
    def test_random_returns_correct_value(self, mocker):
        number = 72

        mocker.get(URL, json={"random_number": number})

        result = Random().getRandom()

        self.assertEqual(result, number)
