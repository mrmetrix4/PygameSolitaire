from logging import getLogger

import pygame
from enum import Enum
from shared import sprites, states


class CardType(Enum):
    HEARTS = 'H'
    SPADES = 'S'
    DIAMONDS = 'D'
    CLUBS = 'C'


class Card:

    def __init__(self, card_dict) -> None:
        self.logger = getLogger(__name__)
        self.logger.debug(f'Card class called with {card_dict=}')

        self.name = card_dict['name'][4:-4]
        self.type, self.number = self.parse_name()

        self.card_surf = self.init_sprite(card_dict)

    def __str__(self) -> str:
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
                raise ValueError(f'Unexpected card value {number_str}')

        return card_type, number

    @staticmethod
    def init_sprite(card_dict) -> (pygame.Rect, pygame.Surface):
        card_rect = pygame.Rect(
            int(card_dict['x']),
            int(card_dict['y']),
            int(card_dict['width']),
            int(card_dict['height'])
        )
        card_surf = pygame.Surface(card_rect.size).convert_alpha()
        card_surf.blit(sprites.cards_sprite_sheet, (0, 0), card_rect)
        color_key = card_surf.get_at((0, 0))
        card_surf.set_colorkey(color_key)
        return card_surf

    def draw(self, **kwargs):
        states.game.screen.blit(self.card_surf, self.card_surf.get_rect(**kwargs))
