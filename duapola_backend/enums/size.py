from enum import Enum


class Size(Enum):
    EXTRA_LARGE = 'xl'
    LARGE = 'l'
    MEDIUM = 'm'
    SMALL = 's'
    EXTRA_SMALL = 'xs'

    @classmethod
    def choices(cls):
        return tuple((size.value, size.name) for size in cls)
