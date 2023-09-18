from django import forms
from codecompanionapp import BaseLLM, FilesHandler

class DocumentationHelperForm(forms.Form, BaseLLM.BaseLLM1):

    input_file1 = forms.FileField(
        label='Upload a file',
        help_text='maximum 5MB'
    )
    input_file2 = forms.FileField(
        label='Upload a file',
        help_text='maximum 5MB'
    )
    input_file3 = forms.FileField(
        label='Upload a file',
        help_text='maximum 5MB'
    )
    base_fields = [input_file1,input_file2,input_file3]

    def create_message_CodeOptimizer(self, input_message):
        message = "" + input_message
        return message
    
    def generate_chat_completion(self, input_file, max_tokens=100):

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
            headers = DocumentationHelperForm.get_headers(self)
            message = DocumentationHelperForm.create_message_CodeOptimizer(self, file_data)
            data = DocumentationHelperForm.get_data(self, messages=message)

            if max_tokens is not None:
                data["max_tokens"] = max_tokens

            response = DocumentationHelperForm.get_response(self, headers, data)
        else:
            file_data = "NO DATA"
            response = file_data
            return response
        
        print(response)

        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            raise Exception(f"Error {response.status_code}: {response.text}")
