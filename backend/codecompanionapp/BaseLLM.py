import requests
import json
import os
# from bardapi import Bard


class BaseLLM1():

    __API_KEY = ""
    __API_ENDPOINT = ""
    __BARD_TOKEN = ''

    def _get_headers(self):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {BaseLLM1.__API_KEY}",
        }
        return headers

    def _get_data(self, messages, model="gpt-3.5-turbo-0613", temperature=1):
        data = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
        }
        return data

    def _get_response(self, headers, data):
        response = requests.post(BaseLLM1.__API_ENDPOINT, headers=headers, data=json.dumps(data))
        return response