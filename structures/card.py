from pydantic import BaseModel, validator
from enum import Enum, auto


class CardType(Enum):
    HEARTS = auto()
    SPADES = auto()
    DIAMONDS = auto()
    CLUBS = auto()


class Card(BaseModel):
    number: int
    type: CardType

    @validator('number')
    def validate_number(cls, v):
        if v < 1 or v > 13:
            raise ValueError('Card number must be 0 to 13')
        return v
