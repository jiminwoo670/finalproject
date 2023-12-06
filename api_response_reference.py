import requests
from pprint import pprint
import json

categories_url = "https://opentdb.com/api_category.php"
response = requests.get(categories_url)
pprint(response.json())
with open("categories.json","w") as categories:
    json.dump(response.json(),categories,indent=4)

questions_url = "https://opentdb.com/api.php?amount=10&category=21"
response = requests.get(questions_url)
with open("questions_url.json","w") as questions:
    json.dump(response.json(),questions,indent=4)