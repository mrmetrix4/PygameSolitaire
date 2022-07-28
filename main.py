import logging

import pygame
import pygame.freetype

from constants import misc, settings, locations
from states.game import Game

pygame.init()


def main():
    screen = pygame.display.set_mode((locations.WIDTH, locations.HEIGHT))

    clock = pygame.time.Clock()

    pygame.display.set_caption(settings.GAME_CAPTION)

    logging.basicConfig(
        filename=settings.LOG_FILE_NAME,
        encoding='utf-8',
        level=settings.LOG_LEVEL
    )

    game = Game()

    running_loop = True
    while running_loop:
        clock.tick(misc.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_loop = False

        game.update(screen)

        pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    main()
