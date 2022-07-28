import pygame

from constants import locations
from structures.card import Card


class Column:
    def __init__(self, idx, card_back_sprite, cards):
        self.idx = idx
        self.card_back_sprite: pygame.Surface = card_back_sprite
        self.cards: list[Card] = cards

    def draw_column(self, screen):
        center_x = locations.ROW_ZERO_CENTER_X[self.idx]
        for i, c in enumerate(self.cards):
            center_y = 330 + i * 50
            if c.revealed:
                c.draw(screen, center=(center_x, center_y))
            else:
                back_rect = self.card_back_sprite.get_rect(
                    center=(center_x, center_y)
                )
                screen.blit(self.card_back_sprite, back_rect)
