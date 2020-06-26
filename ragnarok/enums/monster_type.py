from enum import Enum


class MonsterTypeEnum(Enum):
    LEGENDARY = 'legendary'
    EPIC = 'epic'
    RARE = 'rare'
    NORMAL = 'normal'

    @classmethod
    def choices(cls):
        return tuple((monster_type.value, monster_type.name.capitalize()) for monster_type in cls)
