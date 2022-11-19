from enum import Enum


class TypeOfRemitter(Enum):
    AI = "AI"
    ME = "ME"


def logger(who: TypeOfRemitter, message):
    if (who == TypeOfRemitter.ME):
        print('👨: {}'.format(message))
    elif (who == TypeOfRemitter.AI):
        print('👩: {}'.format(message))
