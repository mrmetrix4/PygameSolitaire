import logging
import random
import xml.etree.ElementTree as ET

import pygame
import pygame.freetype

import settings
import global_sprites
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

    global_sprites.cards_sprite_sheet = (
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

    global_sprites.card_back_sprite = (
        pygame.image.load('assets/Cards Asset/boardgamePack_v2/PNG/Cards/cardBack_blue4.png')
        .convert_alpha()
    )

    global_sprites.card_slot_sprite = (
        pygame.image.load('assets/Cards Asset/custom_made/card_slot.png')
        .convert_alpha()
    )


def main():
    clock = pygame.time.Clock()
    init()

    running_loop = True
    while running_loop:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_loop = False

        SCREEN.blit(global_sprites.card_back_sprite, (30, 30))
        SCREEN.blit(global_sprites.card_back_sprite, (33, 30))
        SCREEN.blit(global_sprites.card_back_sprite, (36, 30))
        SCREEN.blit(global_sprites.card_back_sprite, (39, 30))

        example_rect = global_sprites.card_back_sprite.get_rect(topleft=(0, 30))

        for x in range(4):
            _ = global_sprites.card_slot_sprite.get_rect(midright=(x * 200 + 650, example_rect.centery))
            SCREEN.blit(global_sprites.card_slot_sprite, _)

        sample_card_rect = settings.card_deck[0].card_surf.get_rect(center=_.center)
        SCREEN.blit(settings.card_deck[0].card_surf, sample_card_rect)

        pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    main()
