class GlobalConfiguration:

    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = super().__new__(self)
        return self.instance

    def set_language(self, type_of_language):
        self.type_of_language = type_of_language

    def get_language(self):
        return self.type_of_language

    def set_recognizer(self, type_of_recognizer):
        self.type_of_recognizer = type_of_recognizer

    def get_recognizer(self):
        return self.type_of_recognizer
    
    def set_project_path(self, path):
        self.project_path = path
    
    def get_project_path(self):
        return self.project_path