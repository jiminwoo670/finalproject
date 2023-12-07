import html

from get_question import GetQuestions, FormatQuestions
from players import Players
from player_individual import PlayerIndividual

class PlayGame:
    def __init__(self,players):
        self.players = players
        self.difficulty = ["easy","medium","hard"]
        self.general_knowledge_index = [0,3,6,9,12,15,18]
        self.science_index = [1,4,7,10,13,16,19]
        self.entertainment_index = [2,5,8,11,14,17,20]


    def play_round(self):
        question = GetQuestions()

        for player in self.players:
            score = player.get_player_score()
            print(player.return_player_name(), "   ",score)

        for player in self.players:
            if player.get_player_score() in self.general_knowledge_index:
                difficulty = int(input("On a scale of 1 to 3 how well do you know general knowledge?")) -1
                question_json = question.get_question("general_knowledge",self.difficulty[difficulty]).json()
                format = FormatQuestions(question_json["results"][0])
                print(format.return_question())
                choices = format.shuffle_choices()
                for choice_index, choice in enumerate(choices):
                    print(f"{choice_index+1}.{html.unescape(choice)}")
                answer_choice_index = int(input("What is your answer choice (choose 1 to 4):")) -1
                answer_choice = choices[answer_choice_index]
                correct = format.check_correct_answer(answer_choice)
                if correct == True:
                    player.player_individual_points(difficulty+1)













if __name__ == "__main__":
    players = Players() # Add more players if needed
    players.add_players()
    quiz_game = PlayGame(players.return_player_objects())

    while not quiz_game.play_round():
        pass  # Continue playing rounds until a player reaches 20 points