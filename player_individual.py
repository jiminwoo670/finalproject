class PlayerIndividual:
    def __init__(self,name):
        """
        puts the name and the score of the player as an attribute
        :param name: gets individual player name as argument
        """
        self.name = name
        self.score = 0

    def return_player_name(self):
        """
        :return: the name of player
        """
        return self.name

    def get_player_score(self):
        """
        :return: score of player
        """
        return self.score

    def get_player_object_dict(self):
        """
        this function is used for the name of player and score, the name is the key and the score is value
        :return: dictionary
        """
        return {"name": self.name, "score": self.score}

    def player_individual_points(self,points):
        """
        :param points: ammount of points to add to score
        :return: the added points
        """
        self.score += points

