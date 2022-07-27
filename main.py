import logging

import pygame
import pygame.freetype

from constants import colors, misc, locations, settings
from shared import states
from states.game import Game

pygame.init()

SCREEN = pygame.display.set_mode((locations.WIDTH, locations.HEIGHT))
BASE_FONT = pygame.freetype.SysFont(None, misc.FONT_SIZE)


def init() -> None:
    logging.basicConfig(
        filename=settings.LOG_FILE_NAME,
        encoding='utf-8',
        level=settings.LOG_LEVEL
    )

    pygame.display.set_caption(settings.GAME_CAPTION)
    SCREEN.fill(colors.BACKGROUND_GRAY)

    states.game = Game()


def main():
    clock = pygame.time.Clock()
    init()

    running_loop = True
    while running_loop:
        clock.tick(misc.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_loop = False

        SCREEN.blit(states.game.card_back_sprite, (30, 30))
        SCREEN.blit(states.game.card_back_sprite, (33, 30))
        SCREEN.blit(states.game.card_back_sprite, (36, 30))
        SCREEN.blit(states.game.card_back_sprite, (39, 30))

        example_rect = states.game.card_back_sprite.get_rect(topleft=(0, 30))

        for x in range(4):
            _ = states.game.card_slot_sprite.get_rect(midright=(x * 200 + 650, example_rect.centery))
            SCREEN.blit(states.game.card_slot_sprite, _)

        sample_card_rect = states.game.card_deck[0].card_surf.get_rect(center=_.center)
        SCREEN.blit(states.game.card_deck[0].card_surf, sample_card_rect)

        pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    main()
