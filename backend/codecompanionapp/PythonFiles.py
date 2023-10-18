from codecompanionapp.FilesHandler import FileHandler

class PythonFile(FileHandler):

    __file_type = "Python"

    def get_file_type():
        return PythonFile.__file_type