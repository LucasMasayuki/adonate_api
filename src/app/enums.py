from enum import Enum

class TagType(Enum):
    PURPOSE = "purpose"
    ITEM = "item"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)