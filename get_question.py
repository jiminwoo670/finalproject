import requests
import random
import html
class GetQuestions:
    def __init__(self):
        self.category_general_knowledge = [9,20,21,22,23,24,25,28]
        self.category_entertainment = [11,12,13,14,15,26,29,32]
        self.category_science = [17,18,19,30]


    def get_question(self,category,difficulty):
        category_id = None
        if category == "general_knowledge":
            category_id = random.choice(self.category_general_knowledge)
        if category == "entertainment":
            category_id = random.choice(self.category_entertainment)
        if category == "science":
            category_id = random.choice(self.category_science)

        return requests.get(f"https://opentdb.com/api.php?amount=1&category={category_id}&difficulty={difficulty}&type=multiple")

class FormatQuestions:
    def __init__(self,json):
        self.correct_answer = json["correct_answer"]
        self.question = json["question"]
        self.incorrect_answers = json["incorrect_answers"]
        self.choices = []

    def return_question(self):
        return html.unescape(self.question)

    def shuffle_choices(self):
        choices = self.incorrect_answers
        correct = self.correct_answer
        choices.append(correct)
        return choices

    def check_correct_answer(self,answer_choice):
        if answer_choice == self.correct_answer:
            return True
        else:
            return False
