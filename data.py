import requests

class Data:
    def __init__(self):
        self.parameters = {
            "amount": 10,
            "type": "boolean",
            "category":18
        }
        self.url = "https://opentdb.com/api.php"
        self.question_data = ""
        
    def get_data(self):     
        response = requests.get(url=self.url, params=self.parameters)
        response.raise_for_status()
        data = response.json()
        self.question_data = data["results"]

