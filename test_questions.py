from get_question import GetQuestions
from pprint import pprint

def test_getting_question():
    """
    tests if the generating questions class works
    """
    question = GetQuestions()
    response = question.get_question("science","medium")
    pprint(response.json())


def main():
    test_getting_question()


main()
