import pygame
from enum import Enum


class CardType(Enum):
    HEARTS = 'H'
    SPADES = 'S'
    DIAMONDS = 'D'
    CLUBS = 'C'


class Card:

    def __init__(self, card_dict):
        self.name = card_dict['name'][4:-4]
        self.type, self.number = self.parse_name()

    def __str__(self):
        return f'{self.name}'

    def parse_name(self) -> (CardType, int):
        card_type = CardType(self.name[0])
        number_str = self.name[-1]
        match number_str:
            case '0':
                number = 10
            case 'J':
                number = 11
            case 'Q':
                number = 12
            case 'K':
                number = 13
            case 'A':
                number = 14
            case num if num.isdigit():
                number = int(num)
            case _:
                raise ValueError('Unexpected card value')

        return card_type, number
