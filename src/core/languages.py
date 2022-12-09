import json
from enum import Enum
from src.core.global_configuration import GlobalConfiguration
from src.core.global_paths import GlobalPaths


class TypeOfLanguage(Enum):
    SPANISH = "GOOGLE"
    ENGLISH = "WHISPER"
    PORTUGUESE = "PORTUGUESE"


class Translate:

    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = super().__new__(self)
            type_of_language = GlobalConfiguration().get_language()
            if type_of_language == TypeOfLanguage.ENGLISH:
                self.language_file = json.load(open(GlobalPaths.i18n_en_json))
            elif type_of_language == TypeOfLanguage.SPANISH:
                self.language_file = json.load(open(GlobalPaths.i18n_es_json))
            elif type_of_language == TypeOfLanguage.PORTUGUESE:
                self.language_file = json.load(open(GlobalPaths.i18n_pt_json))
        return self.instance

    def get_world(self, key):
        return self.language_file[key]
