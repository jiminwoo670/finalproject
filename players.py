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

    def player_stats_json(self):
        """
        puts the user's name and score into a json file to make a leaderboard
        """
        leader_board_json = "player_stats.json"
        try:
            with open(leader_board_json, "r") as player_stats_file:
                existing_data = json.load(player_stats_file)
        except FileNotFoundError:
            # if file does not exist yet make a emtpy list
            existing_data = []

        if not isinstance(existing_data, list):
            existing_data = []

        for player in self.players:
            existing_data.append(player.get_player_object_dict())

        with open(leader_board_json, "w") as player_stats_file:
            json.dump(existing_data, player_stats_file, indent=4)

        sorted_players = sorted(existing_data, key=lambda x: x['score'], reverse=True)
        rank = 1
        for player in sorted_players:
            print(f"{rank}. {player['name']} - Score: {player['score']}")
            rank += 1




    def delete_player(self):





    def return_player_objects(self):
        return self.players


