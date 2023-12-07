import requests
from players import Players

class Game:
    def __init__(self):
        self.category_general_knowledge_lst = [9,20,21,22,23,24,25,28]
        self.category_entertainment = [11,12,13,14,15,26,29,32]
        self.category_science = [17,18,19,30]
        self.players = Players()

    def test_getting_players(self):
        return self.players



