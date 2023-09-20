from django import forms
from codecompanionapp import BaseLLM, FilesHandler

class LetterGeneratorForm(forms.Form, BaseLLM.BaseLLM1):
    
    input_code = forms.CharField(widget=forms.TextInput(attrs={ 'required': 'true' }))
    base_fields = [input_code]
    
    def create_message_LetterGenerator(self, input_message):
        message = "" + input_message
        return message
    
    def generate_chat_completion(self, input_file, input_message, max_tokens=100):

        print(type(input_file))
        if type(input_file) == type(""):
            file_lines = len(input_file)
        else:
            file_lines = FilesHandler.FileHandler.number_of_lines(input_file)
        print(file_lines)
        if(file_lines > 10):
            if type(input_file) == type(""):
                file_data = input_file
            else:
                file_data = FilesHandler.FileHandler.read_file(input_file)
            print(file_data)
            headers = LetterGeneratorForm.get_headers(self)
            message = LetterGeneratorForm.create_message_LetterGenerator(self, input_message)
            data = LetterGeneratorForm.get_data(self, messages=message)

            if max_tokens is not None:
                data["max_tokens"] = max_tokens

            response = LetterGeneratorForm.get_response(self, headers, data)
        else:
            file_data = "NO DATA"
            response = file_data
            return response
        
        print(response)

        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            raise Exception(f"Error {response.status_code}: {response.text}")