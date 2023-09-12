import json

import requests


class Request:
    @staticmethod
    def send(log_model):
        try:
            url = "http://127.0.0.1:5000/log"
            log_model_json = json.dumps(log_model.__dict__)
            header = {'Content-Type': 'application/json'}
            response = requests.post(url, data=log_model_json, headers=header)

            if response.status_code != 200:
                print("Log failed", response.text)
            print("Log sends successfully !!", "Response:\n" + response.text)
        except Exception as e:
            print("\nError to connect to server :(")