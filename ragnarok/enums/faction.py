from enum import Enum


class FactionEnum(Enum):
    ROCK = 'rock'
    PAPER = 'paper'
    SCISSOR = 'scissor'
    WHITE = 'white'
    BLACK = 'black'

    @classmethod
    def choices(cls):
        return tuple((faction.value, faction.name.capitalize()) for faction in cls)
