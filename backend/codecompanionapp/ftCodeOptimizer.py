from django import forms
import requests
import json
import os
from bardapi import Bard

API_KEY = ""
API_ENDPOINT = ""
BARD_TOKEN = ''

class CodeOptimizerForm(forms.Form):
    input_code = forms.CharField(widget=forms.TextInput(attrs={ 'required': 'true' }))
    base_fields = [input_code]

    def generate_chat_completion(self, messages, model="gpt-3.5-turbo-0613", temperature=1, max_tokens=100):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}",
        }

        data = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
        }

        if max_tokens is not None:
            data["max_tokens"] = max_tokens

        response = requests.post(API_ENDPOINT, headers=headers, data=json.dumps(data))
        print(response)

        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            raise Exception(f"Error {response.status_code}: {response.text}")
