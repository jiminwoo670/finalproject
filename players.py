from player_individual import PlayerIndividual
class Players:
    def __init__(self):
        self.players = []

    def add_players(self):
        """
        Asks name of player and appends name
        """
        player_count = input("How many players for this game:")
        for i in range(int(player_count)):
            name = input("What is your name:")
            self.players.append(PlayerIndividual(name))

    def find_player(self,name):
        """
        finds player
        :param name: name of player trying to find
        :return: name of player if found, no name found if no name found
        """
        found = False
        for player in self.players:
            if player.return_player_name() == name:
                return name
            else:
                return"Player not found"

    def return_player_objects(self):
        return self.players


