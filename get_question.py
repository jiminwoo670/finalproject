import requests
import random
import html
class GetQuestions:
    def __init__(self):
        self.category_general_knowledge = [9,21,22,23,24]
        self.category_entertainment = [11,12,14,15,26,32]
        self.category_science = [17,18,19,30]


    def which_category(self,score):
        general_knowledge_index = [0, 3, 6, 9, 12, 15, 18]
        science_index = [1, 4, 7, 10, 13, 16, 19]
        entertainment_index = [2, 5, 8, 11, 14, 17, 20]
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
        category_id = None
        if category == "general_knowledge":
            category_id = random.choice(self.category_general_knowledge)
        if category == "entertainment":
            category_id = random.choice(self.category_entertainment)
        if category == "science":
            category_id = random.choice(self.category_science)

        return requests.get(f"https://opentdb.com/api.php?amount=1&category={category_id}&difficulty={difficulty}&type=multiple")

    """def get_single_question(self,question_json):
        questions = question_json["results"]
        question = random.choice(questions)
        return question"""




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


