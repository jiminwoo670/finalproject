import requests
import random
import html
class GetQuestions:
    def __init__(self):
        self.category_general_knowledge = [9,21,22,23,24]
        self.category_entertainment = [11,12,14,15,26,32]
        self.category_science = [17,18,19,30]


    def which_category(self,score):
        """
        this method returns a category depending on the score of a player
        :param score: a score of a player is passed as an arguement
        :return: category
        """
        # score-category indexes
        general_knowledge_index = [0, 3, 6, 9, 12, 15, 18]
        science_index = [1, 4, 7, 10, 13, 16, 19]
        entertainment_index = [2, 5, 8, 11, 14, 17, 20]
        # Iterates through each category indexes and returns category if found, if not, moves on to next
        for i in general_knowledge_index:
            if score == i:
                return "general_knowledge"

        for i in science_index:
            if score == i:
                return "science"

        for i in entertainment_index:
            if score == i:
                return "entertainment"




    def get_question(self, category, difficulty):
        """
        this method pulls a random question from api depending on its category and difficulty
        :param category: players category depends on the score
        :param difficulty: player chooses difficulty
        :return: question
        """
        # set category_id as "none" first
        category_id = None
        # gets the category argument and places category_id to its random subcategory
        if category == "general_knowledge":
            category_id = random.choice(self.category_general_knowledge)
        if category == "entertainment":
            category_id = random.choice(self.category_entertainment)
        if category == "science":
            category_id = random.choice(self.category_science)

        # pulls from api and then returns the question
        return requests.get(f"https://opentdb.com/api.php?amount=1&category={category_id}&difficulty={difficulty}&type=multiple")

class FormatQuestions:
    def __init__(self,json):
        """
        gets the json of a question and makes the correct answer, question, incorrect answer, and choices as parameters
        :param json: the json of a singular question is an argument
        """
        self.correct_answer = json["correct_answer"]
        self.question = json["question"]
        self.incorrect_answers = json["incorrect_answers"]
        self.choices = []

    def return_question(self):
        """
        :return: the correctly formmated question
        """
        # we need to put it through the html.unescape function first because the question will look like gibberish if we don't
        return html.unescape(self.question)

    def shuffle_choices(self):
        """
        this method randomly shuffles the answer choices. If we just append it, the correct answer will always be the last one
        :return: shuffled choices
        """
        choices = self.incorrect_answers
        correct = self.correct_answer
        choices.append(correct)
        return choices

    def check_correct_answer(self,answer_choice):
        """
        checks if the answer choice the user inputted is correct
        :param answer_choice: user answer choice
        :return: if correct or not
        """
        if answer_choice == self.correct_answer:
            return True
        else:
            return False


