import random
import pygame
import xml.etree.ElementTree as ET

from constants import paths
from shared import sprites
from structures.card import Card


class Game:

    def _init_cards(self):
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

    def __init__(self, screen: pygame.Surface):
        self.screen = screen

        self.card_deck: list[Card] = []
        self.card_back_sprite: pygame.Surface = None
        self.card_slot_sprite: pygame.Surface = None

        self._init_cards()
