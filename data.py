import requests

param = {
    "amount": 10,
    "type": "boolean"
}
response = requests.get("https://opentdb.com/api.php?amount=10&category=20&type=boolean", params=param)
response.raise_for_status()
data_dict = response.json()
question_data = data_dict["results"]

