class PlayerIndividual:
    def __init__(self,name):
        self.name = name
        self.score = 0

    def return_player_name(self):
        return self.name

    def get_player_score(self):
        return self.score

    def player_individual_points(self,points):
        self.score += points

