import pygame
import pygame.freetype
import xml.etree.ElementTree as ET
from constants.colors import *
from structures.card import Card

pygame.init()

FPS = 60
WIDTH, HEIGHT = (1280, 720)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BASE_FONT = pygame.freetype.SysFont(None, 24)

tree = ET.parse('assets/Cards Asset/boardgamePack_v2/Spritesheets/playingCards.xml')
root = tree.getroot()

cards_sprites = {}
for child in root:
    cards_sprites[child.attrib['name'][4:-4]] = child.attrib


def init() -> None:
    pygame.display.set_caption('PygameSolitaire')
    SCREEN.fill((200, 200, 200))


def main():
    clock = pygame.time.Clock()
    init()

    running_loop = True
    while running_loop:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_loop = False

        test_sheet = pygame.image.load('assets/Cards Asset/boardgamePack_v2/Spritesheets/playingCards.png').convert_alpha()
        SCREEN.blit(test_sheet, (30, 30))

        # sample_card = pygame.transform.rotozoom(
        #     pygame.image.load('assets/card_sprites/club/cardClubs_4.png').convert_alpha(),
        #     0,
        #     0.3
        # )
        # sample_card_rect = sample_card.get_rect()
        # sample_card_rect.center = (WIDTH / 2, HEIGHT / 2)
        #
        # pseudo_rect = pygame.Rect(sample_card_rect.left - 1, sample_card_rect.top - 1,
        #                           sample_card_rect.width + 2, sample_card_rect.height + 2)
        #
        # pygame.draw.rect(SCREEN, Color('black'), pseudo_rect, 1)
        #
        # SCREEN.blit(sample_card, sample_card_rect)
        #
        # pygame.draw.aaline(SCREEN, Color('black'), (WIDTH / 2, 0), (WIDTH / 2, HEIGHT))
        # pygame.draw.aaline(SCREEN, Color('black'), (0, HEIGHT / 2), (WIDTH, HEIGHT / 2))

        pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    main()
