from django import forms
from codecompanionapp import BaseLLM

class UnitTestGeneratorForm(forms.Form, BaseLLM.BaseLLM1):
    
    input_code = forms.CharField(widget=forms.TextInput(attrs={ 'required': 'true' }))
    base_fields = [input_code]
    
    def create_message_UnitTestGenerator(self, input_code):
        message = "Generate unit test for this piece of code. \n" + input_code
        return message
    
    def generate_chat_completion(self, input_message, max_tokens=100):

        headers = UnitTestGeneratorForm._get_headers(self)
        message = UnitTestGeneratorForm.create_message_UnitTestGenerator(self, input_message)
        data = UnitTestGeneratorForm._get_data(self, messages=message)

        if max_tokens is not None:
            data["max_tokens"] = max_tokens

        response = UnitTestGeneratorForm._get_response(self, headers, data)
        print(response)

        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            raise Exception(f"Error {response.status_code}: {response.text}")