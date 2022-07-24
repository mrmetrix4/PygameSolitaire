import logging
import random
import xml.etree.ElementTree as ET

import pygame
import pygame.freetype

import settings
from structures.card import Card

pygame.init()

FPS = 60
WIDTH, HEIGHT = (1280, 720)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BASE_FONT = pygame.freetype.SysFont(None, 24)


def init() -> None:
    logging.basicConfig(filename='Solitaire.log', encoding='utf-8', level=settings.log_level)

    pygame.display.set_caption('PygameSolitaire')
    SCREEN.fill((200, 200, 200))

    settings.sprite_sheet = (
        pygame.image.load('assets/Cards Asset/boardgamePack_v2/Spritesheets/playingCards.png')
        .convert_alpha()
    )
    cards_xml_tree = ET.parse('assets/Cards Asset/boardgamePack_v2/Spritesheets/playingCards.xml')
    cards_xml_tree_root = cards_xml_tree.getroot()
    for child in cards_xml_tree_root:
        if child.attrib['name'] == 'cardJoker.png':
            continue
        settings.card_deck.append(Card(child.attrib))
    random.shuffle(settings.card_deck)


def main():
    clock = pygame.time.Clock()
    init()

    running_loop = True
    while running_loop:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_loop = False

        SCREEN.blit(settings.sprite_sheet, (0, 0))
        card_name, _ = BASE_FONT.render(str(settings.card_deck[0]))
        SCREEN.blit(card_name, (0, 0))
        SCREEN.blit(settings.card_deck[0].card_surf, (30, 30))

        pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    main()
