import requests


def get_question():
    data = requests.get(
        "https://opentdb.com/api.php?amount=10&category=11&difficulty=easy&type=boolean")
    return data.json()["results"]
