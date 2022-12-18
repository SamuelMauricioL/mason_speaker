import os
import json
from src.utils.file_explorer import FileExplorer
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
            self.file_explorer = FileExplorer()
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
        self.project_path = self.file_explorer.find_folder()

    def get_project_path(self):
        return self.project_path

    def set_feature(self):
        self.feature_path = self.file_explorer.find_folder(self.project_path)

    def get_feature_path(self):
        return self.feature_path
