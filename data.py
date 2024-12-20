import requests
parameters = {
    "amount": 10,
    "type": "boolean",
}
api = requests.get(url="https://opentdb.com/api.php",params=parameters)
api.raise_for_status()
quiz_dic = api.json()["results"]


question_data = quiz_dic
