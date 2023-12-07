from player_individual import PlayerIndividual
class Players:
    def __init__(self):
        self.players = []

    def add_player(self):
        """
        Asks name of player and appends name
        """
        name = input("What is your name:")
        self.players.append(PlayerIndividual(name))

    def return_player_objects(self):
        return self.players

    def find_player(self,name):
        """
        finds player
        :param name: name of player trying to find
        :return: name of player if found, no name found if no name found
        """
        for player_name in self.players:
            if player_name == name:
                return name
            else:
                return"Player not found"

