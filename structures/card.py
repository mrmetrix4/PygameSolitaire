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

    class Config:
        allow_mutation = False

    def __gt__(self, other):
        if other.type != self.type:
            raise TypeError("Can't compare cards of different types")
        return other.number > self.number

    @validator('number')
    def validate_number(cls, v):
        if v < 1 or v > 13:
            raise ValueError('Card number must be 0 to 13')
        return v

    def draw(self):
        pass
    # TODO: Card.draw()
