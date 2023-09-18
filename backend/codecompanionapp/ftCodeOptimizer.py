from django import forms
from codecompanionapp.BaseLLM import BaseLLM1

class CodeOptimizerForm(forms.Form, BaseLLM1):
    
    input_code = forms.CharField(widget=forms.TextInput(attrs={ 'required': 'true' }))
    base_fields = [input_code]
    
    def create_message_CodeOptimizer(self, input_message):
        message = "" + input_message
        return message
    
    def generate_chat_completion(self, input_message, max_tokens=100):

        headers = CodeOptimizerForm.get_headers()
        message = CodeOptimizerForm.create_message_CodeOptimizer(input_message)
        data = CodeOptimizerForm.get_data(messages=message)

        if max_tokens is not None:
            data["max_tokens"] = max_tokens

        response = CodeOptimizerForm.get_response(headers, data)
        print(response)

        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            raise Exception(f"Error {response.status_code}: {response.text}")
