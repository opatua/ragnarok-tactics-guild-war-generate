from enum import Enum


class ElementEnum(Enum):
    FIRE = 'fire'
    EARTH = 'earth'
    WATER = 'water'
    WIND = 'wind'
    DARK = 'dark'
    HOLY = 'holy'

    @classmethod
    def choices(cls):
        return tuple((element.value, element.name.capitalize()) for element in cls)
