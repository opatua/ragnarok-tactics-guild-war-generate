from enum import Enum


class CartStatus(Enum):
    PENDING = 'pending'
    COMPLETED = 'completed'

    @classmethod
    def choices(cls):
        return tuple((cart.value, cart.name) for cart in cls)
