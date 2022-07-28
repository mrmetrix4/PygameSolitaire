import pygame

from constants import locations
from structures.card import CardType, Card


class Slot:
    def __init__(self, idx, card_type, card_slot_sprite):
        self.idx = idx
        self.card_type: CardType = card_type
        self.card_slot_sprite: pygame.Surface = card_slot_sprite
        self.last_card: Card = None

    def draw_slot(self, screen):
        slot_rect = self.card_slot_sprite.get_rect(
            center=(locations.ROW_ZERO_CENTER_X[3 + self.idx], locations.ROW_ZERO_CENTER_Y)
        )
        screen.blit(self.card_slot_sprite, slot_rect)
        if self.last_card:
            self.last_card.draw(screen, center=slot_rect.center)
