import logging

import pygame
import pygame.freetype

from constants import misc, settings
from shared import states
from states.game import Game

pygame.init()


def main():
    clock = pygame.time.Clock()

    pygame.display.set_caption(settings.GAME_CAPTION)

    logging.basicConfig(
        filename=settings.LOG_FILE_NAME,
        encoding='utf-8',
        level=settings.LOG_LEVEL
    )

    states.game = Game()

    running_loop = True
    while running_loop:
        clock.tick(misc.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_loop = False

        states.game.draw_columns()

        pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    main()
