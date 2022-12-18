import os
import json
from tkinter import *
from tkinter import filedialog
from src.core.global_paths import GlobalPaths


class GlobalConfiguration:

    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = super().__new__(self)

            global_configuration = json.load(
                open(GlobalPaths.global_configuration_json),
            )

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
        self.__init_file_explorer()
        self.file_explorer.after_idle(self.__set_project_path)
        self.file_explorer.mainloop()

    def __set_project_path(self):
        self.project_path = filedialog.askdirectory()
        self.__destroy_file_explorer()

    def get_project_path(self):
        return self.project_path

    def set_feature(self):
        self.__init_file_explorer()
        self.file_explorer.after_idle(self.__set_feature_path)
        self.file_explorer.mainloop()

    def __set_feature_path(self):
        self.feature_path = filedialog.askdirectory(
            initialdir=self.project_path)
        self.__destroy_file_explorer()

    def get_feature_path(self):
        return self.feature_path

    def __destroy_file_explorer(self):
        self.file_explorer.destroy()
        self.file_explorer = None

    def __init_file_explorer(self):
        if self.file_explorer == None:
            self.file_explorer = Tk()
