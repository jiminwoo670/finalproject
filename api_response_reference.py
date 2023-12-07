import requests
from pprint import pprint
import json

categories_url = "https://opentdb.com/api_category.php"
response = requests.get(categories_url)
pprint(response.json())
with open("categories.json","w") as categories:
    json.dump(response.json(),categories,indent=4)

questions_url = "https://opentdb.com/api.php?amount=1&category=20&difficulty=medium&type=multiple"
response = requests.get(questions_url)
print(response.json())
with open("question_test_url.json","w") as questions:
    json.dump(response.json(),questions,indent=4)