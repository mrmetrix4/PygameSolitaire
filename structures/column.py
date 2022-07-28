import pygame

from structures.card import Card


class Column:
    def __init__(self, idx, card_back_sprite, cards):
        self.idx = idx
        self.card_back_sprite: pygame.Surface = card_back_sprite
        self.cards: list[Card] = cards

    def draw_column(self, screen):
        pass
