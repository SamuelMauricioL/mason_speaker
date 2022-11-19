class GlobalConfiguration:

    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = super().__new__(self)
        return self.instance

    def set_language(self, type_of_language):
        self.type_of_language = type_of_language

    def getLanguage(self):
        return self.type_of_language