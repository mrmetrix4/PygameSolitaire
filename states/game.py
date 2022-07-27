import random
import xml.etree.ElementTree as ET

import pygame

from constants import paths, locations, colors, misc
from shared import sprites
from structures.card import Card


class Game:
    def __init__(self):
        self.screen: pygame.Surface = pygame.display.set_mode((locations.WIDTH, locations.HEIGHT))
        self.base_font: pygame.freetype.Font = pygame.freetype.SysFont(None, misc.FONT_SIZE)

        self.card_deck: list[Card] = []
        self.card_back_sprite: pygame.Surface = None
        self.card_slot_sprite: pygame.Surface = None
        self.columns: list[list[Card]] = []

        self._init_screen()
        self._init_sprites_and_deck()
        self._init_slots()
        self._init_columns()

    def _init_sprites_and_deck(self):
        sprites.cards_sprite_sheet = (
            pygame.image.load(paths.CARDS_SPRITE_SHEET)
            .convert_alpha()
        )
        cards_xml_tree = ET.parse(paths.CARDS_SPRITE_XML)
        cards_xml_root = cards_xml_tree.getroot()
        for child in cards_xml_root:
            if child.attrib['name'] == 'cardJoker.png':
                continue
            self.card_deck.append(Card(child.attrib))
        random.shuffle(self.card_deck)

        self.card_back_sprite = (
            pygame.image.load(paths.CARD_BACK_SPRITE)
            .convert_alpha()
        )

        self.card_slot_sprite = (
            pygame.image.load(paths.CARD_SLOT_SPRITE)
            .convert_alpha()
        )

    def _init_slots(self):
        for x_pos in locations.SLOTS_CENTER_X:
            slot_rect = self.card_slot_sprite.get_rect(center=(x_pos, locations.ROW_ZERO_CENTER_Y))
            self.screen.blit(self.card_slot_sprite, slot_rect)

    def _init_screen(self):
        self.screen.fill(colors.BACKGROUND_GRAY)

    def _init_columns(self):
        for col in range(7):
            self.columns.append([self.card_deck.pop() for _ in range(col + 1)])

    def draw_columns(self):
        pass
