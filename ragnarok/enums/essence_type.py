from enum import Enum


class EssenceTypeEnum(Enum):
    LEGENDARY = 'legendary'
    EPIC = 'epic'
    RARE = 'rare'

    @classmethod
    def choices(cls):
        return tuple((essence_type.value, essence_type.name.capitalize()) for essence_type in cls)
