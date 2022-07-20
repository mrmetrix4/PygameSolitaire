import pygame
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
    _sprite = None

    class Config:
        allow_mutation = False

    @validator('number')
    def validate_number(cls, v):
        if v < 1 or v > 13:
            raise ValueError('Card number must be 0 to 13')
        return v

    def set_sprite(self, sprite_surface, x, y, width, height):
        rect = pygame.Rect((x, y, width, height))
        image = pygame.Surface(rect.size).convert()
        image.blit(sprite_surface, (0, 0), rect)
        self._sprite = image

    @property(fset=set_sprite)
    def sprite(self):
        return self._sprite

    def draw(self):
        pass
    # TODO: Card.draw()
