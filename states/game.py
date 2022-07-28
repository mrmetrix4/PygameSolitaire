import random
import xml.etree.ElementTree as ET

import pygame

from constants import paths, locations, colors, misc
from structures.card import Card, CardType
from structures.column import Column
from structures.slot import Slot


class Game:
    def __init__(self):
        self.base_font: pygame.freetype.Font = pygame.freetype.SysFont(None, misc.FONT_SIZE)

        self.card_deck: list[Card] = []
        self.card_back_sprite: pygame.Surface = None
        self.card_slot_sprite: pygame.Surface = None
        self.slots: list[Slot] = []
        self.columns: list[Column] = []

        self._init_sprites_and_deck()
        self._init_slots()
        self._init_columns()

    def _init_sprites_and_deck(self):
        self.cards_sprite_sheet = (
            pygame.image.load(paths.CARDS_SPRITE_SHEET)
            .convert_alpha()
        )
        cards_xml_tree = ET.parse(paths.CARDS_SPRITE_XML)
        cards_xml_root = cards_xml_tree.getroot()
        for child in cards_xml_root:
            if child.attrib['name'] == 'cardJoker.png':
                continue
            self.card_deck.append(Card(child.attrib, self.cards_sprite_sheet))
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
        for idx, card_type in enumerate(CardType):
            self.slots.append(Slot(idx, card_type, self.card_slot_sprite))

    def _init_columns(self):
        for col in range(7):
            self.columns.append(
                Column(col, self.card_back_sprite, [self.card_deck.pop() for _ in range(col + 1)])
            )

    def update(self, screen):
        screen.fill(colors.BACKGROUND_GRAY)
        for s in self.slots:
            s.draw_slot(screen)
        for c in self.columns:
            c.draw_column(screen)
