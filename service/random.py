import requests

URL = "http://codechallenge.boohma.com/random"

class Random():
    def getRandom(self):
        response = requests.get(url = URL).json()
        return response["random_number"]