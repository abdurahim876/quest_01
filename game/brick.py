import pygame
import random

from .constants import RED, WIDTH, HEIGHT, WHITE
class Bricks(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40, 15))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x =x
        self.rect.y =y

