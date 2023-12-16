import html

from get_question import GetQuestions, FormatQuestions
from players import Players

from player_individual import PlayerIndividual

class PlayGame:
    def __init__(self,players):
        self.players = players
        self.difficulty = ["easy","medium","hard"]



    def play_round(self):
        question = GetQuestions()

        for player in self.players:
            score = player.get_player_score()
            print(player.return_player_name(), "   ",score)
        # iterates through all players
        for player in self.players:
            print(player.return_player_name(),"'s","   turn")
            # gets which category is chosen based on how many points the player has
            get_category = question.which_category(player.get_player_score())
            # user chooses difficulty of question
            difficulty = int(input("""On a scale of 1 to 3 how well do you know """+get_category+"""?""")) -1
            # makes user input correctly value making it more robust
            while difficulty not in range(0, 3):
                difficulty = int(input("invalid input, please enter number between 1 to 3:"))
            # fetches question from api from the GetQuestions class
            question_json = question.get_question(get_category, self.difficulty[difficulty]).json()
            # sends question into FormatQuestion class to be formatted
            format = FormatQuestions(question_json["results"][0])
            # prints the question
            print(format.return_question())
            # shuffles the answer choices
            choices = format.shuffle_choices()
            # print the answer choices in a neat and orderly fashion
            for choice_index, choice in enumerate(choices):
                print(f"{choice_index+1}.{html.unescape(choice)}")
            # user inputs answer choice
            answer_choice_index = int(input("What is your answer choice (choose 1 to 4):")) -1
            # makes user input correctly value making it more robust
            while answer_choice_index not in range(0,4):
                answer_choice_index = int(input("invalid input, please enter number between 1 to 4:"))

            # gets the user's answer choice by using the number as an index
            answer_choice = choices[answer_choice_index]
            # checks if the answer is correct
            correct = format.check_correct_answer(answer_choice)
            # adds point if answer choice is correct
            if correct == True:
                print("Correct Answer")
                player.player_individual_points(difficulty+1)
            # does nothing if wrong
            else:
                print("Incorrect Answer")
            # ends the game
            if player.get_player_score() >= 2:
                print(f"Congratulations! {player.return_player_name()} has reached 20 points. Game over!")
                leader_board =  players.player_stats_json()
                return True


if __name__ == "__main__":
    players = Players() # instance of Players class
    player_count = players.add_players() # adds players

    quiz_game = PlayGame(players.return_player_objects()) #instance of PlayGame class

    while not quiz_game.play_round():
        pass  # Continue playing rounds until a player reaches 20 points