import pygame.image
import pytest

from constants import paths
from structures.card import Card
from pytest import fixture

pygame.init()
pygame.display.set_mode((0, 0))


@fixture
def card_sprite():
    return pygame.image.load(paths.CARD_BACK_SPRITE).convert_alpha()


def test_card_creation(card_sprite):
    c = Card(
        {
            'name': 'cardSpades7.png',
            'x': 0,
            'y': 0,
            'width': 200,
            'height': 200
        },
        card_sprite
    )


def test_card_faulty_creation(card_sprite):
    with pytest.raises(ValueError):
        Card(
            {
                'name': 'cardspades7.png',
                'x': 0,
                'y': 0,
                'width': 200,
                'height': 200
            },
            card_sprite
        )
