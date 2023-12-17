from player_individual import PlayerIndividual
import json
class Players:
    def __init__(self):
        self.players = []

    def add_players(self,name):
        """
        Asks name of player and appends name
        """

        self.players.append(PlayerIndividual(name))

    def find_player(self,name):
        """
        finds player
        :param name: name of player trying to find
        :return: name of player if found, no name found if no name found
        """
        # iterates through players
        for player in self.players:
            # if a players name is equal to name, it returns the name, if no name is found, return false
            if player.return_player_name() == name:
                return name
            else:
                return"Player not found"

    def player_stats_json(self):
        """
        puts the user's name and score into a json file to make a leaderboard
        """
        # set file name as such
        leader_board_json = "player_stats.json"
        #  try open the file
        try:
            with open(leader_board_json, "r") as player_stats_file:
                # if the file is found, set existing_data variable as the data in the opened file
                existing_data = json.load(player_stats_file)
        except FileNotFoundError:
            # if file does not exist yet make a emtpy list
            existing_data = []

        if not isinstance(existing_data, list):
            existing_data = []
        # loops through the players in the current game and appends them to the existing data
        for player in self.players:
            # the get player object dict makes a dictionary of the player name and score into a dictionary
            existing_data.append(player.get_player_object_dict())

        # opens file to write in it
        with open(leader_board_json, "w") as player_stats_file:
            # dumps the player stats into file
            json.dump(existing_data, player_stats_file, indent=4)
        # uses sort function to create leaderboard
        sorted_players = sorted(existing_data, key=lambda x: x['score'], reverse=True)
        # prints the sorted players neatly
        rank = 1
        for player in sorted_players:
            print(f"{rank}. {player['name']} - Score: {player['score']}")
            rank += 1




    def return_player_objects(self):
        # return the list of player objects
        return self.players


