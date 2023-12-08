from get_question import GetQuestions
from pprint import pprint

def test_getting_question():
    """
    tests if the generating questions class works
    """
    question = GetQuestions()
    response = question.get_question("science","medium")
    pprint(response.json())

def test_difficulty_input_validity():
    question = GetQuestions()
    difficulty = 3
    difficulty = question.check_difficulty_input_validity(difficulty)
    print(difficulty)

def main():
    #test_getting_question()
    test_difficulty_input_validity()


main()
