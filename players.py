from player_individual import PlayerIndividual
import json
class Players:
    def __init__(self):
        self.players = []

    def add_players(self):
        """
        Asks name of player and appends name
        """
        player_count = int(input("How many players for this game:"))
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

    def player_leaderboard(self):
        file_path = "player_stats.json"
        try:
            with open(file_path, "r") as player_stats_file:
                existing_data = json.load(player_stats_file)
        except FileNotFoundError:
            # If the file doesn't exist yet, initialize with an empty list
            existing_data = []

        if not isinstance(existing_data, list):
            existing_data = []

        for player in self.players:
            existing_data.append(player.get_player_object_dict())

        with open(file_path, "w") as player_stats_file:
            json.dump(existing_data, player_stats_file, indent=4)



    def return_player_objects(self):
        return self.players


