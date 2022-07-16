import pygame
import pygame.freetype
from constants.colors import *

pygame.init()

FPS = 60
WIDTH, HEIGHT = (1000, 500)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BASE_FONT = pygame.freetype.SysFont(None, 24)


def init() -> None:
    pygame.display.set_caption('PygameSolitaire')
    SCREEN.fill(WHITE)


def main():
    clock = pygame.time.Clock()
    init()

    running_loop = True
    while running_loop:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_loop = False

        pygame.draw.line(SCREEN, 'black', (WIDTH / 2, 0), (WIDTH / 2, HEIGHT))

        ts, r = BASE_FONT.render("Shall the game begin!")
        r.update((WIDTH - r.width) / 2, HEIGHT / 8, r.width, r.height)

        SCREEN.blit(ts, r)
        pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    main()
