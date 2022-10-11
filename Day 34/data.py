from urllib import response
import requests
question_data = []

response = requests.get(url="https://opentdb.com/api.php?amount=10&category=17&difficulty=medium&type=boolean")
response.raise_for_status()
data = response.json()
results = data["results"]

for item in results:
    q_hold = item["question"]
    ans_hold = item["correct_answer"]
    question = {
        "question": q_hold,
        "correct_answer": ans_hold,
    }
    question_data.append(question)

