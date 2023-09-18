import requests
import json
import os
# from bardapi import Bard


API_KEY = ""
API_ENDPOINT = ""
BARD_TOKEN = ''

class BaseLLM1():

    def get_headers(self):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}",
        }
        return headers

    def get_data(self, messages, model="gpt-3.5-turbo-0613", temperature=1):
        data = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
        }
        return data

    def get_response(self, headers, data):
        response = requests.post(API_ENDPOINT, headers=headers, data=json.dumps(data))
        return response