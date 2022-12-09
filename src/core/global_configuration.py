import os
import json
from tkinter import *
from tkinter import filedialog


class GlobalConfiguration:

    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = super().__new__(self)

            global_configuration = json.load(
                open('./src/core/global_configuration.json'))
            self.project_path = global_configuration['project_path']
            self.feature_path = global_configuration['feature_path']
            self.file_explorer = Tk()
            os.system("clear")
        return self.instance

    def set_language(self, type_of_language):
        self.type_of_language = type_of_language

    def get_language(self):
        return self.type_of_language

    def set_recognizer(self, type_of_recognizer):
        self.type_of_recognizer = type_of_recognizer

    def get_recognizer(self):
        return self.type_of_recognizer

    def set_project(self):
        self.file_explorer.after_idle(self.set_project_path)
        self.file_explorer.mainloop()

    def set_project_path(self):
        self.project_path = filedialog.askdirectory()
        self.file_explorer.destroy()

    def get_project_path(self):
        return self.project_path

    def set_feature(self):
        # self.file_explorer_2 = Tk()
        self.file_explorer.after_idle(self.set_feature_path)
        self.file_explorer.mainloop()

    def set_feature_path(self):
        self.feature_path = filedialog.askdirectory(
            initialdir=self.project_path)
        self.file_explorer.destroy()

    def get_feature_path(self):
        return self.feature_path
