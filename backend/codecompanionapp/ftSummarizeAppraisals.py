from django import forms
import requests
import json
import os
from bardapi import Bard

API_KEY = ""
API_ENDPOINT = ""
BARD_TOKEN = ''

class SummarizeAppraisalsForm(forms.Form):
    input_code = forms.CharField(widget=forms.TextInput(attrs={ 'required': 'true' }))
    base_fields = [input_code]

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

    def get_response(headers, data):
        response = requests.post(API_ENDPOINT, headers=headers, data=json.dumps(data))
        return response
    
    def generate_chat_completion(self, messages, model="gpt-3.5-turbo-0613", temperature=1, max_tokens=100):

        headers = SummarizeAppraisalsForm.get_headers()
        data = SummarizeAppraisalsForm.get_data()

        if max_tokens is not None:
            data["max_tokens"] = max_tokens

        response = SummarizeAppraisalsForm.get_response(headers, data)
        print(response)

        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            raise Exception(f"Error {response.status_code}: {response.text}")
