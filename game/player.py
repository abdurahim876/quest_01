import pygame
from .constants import GREEN, WIDTH, HEIGHT


class Player(pygame.sprite.Sprite):
    player_group = pygame.sprite.Group()
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((125, 20))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT - self.rect.height)



    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
            if self.rect.right < 0:
                self.rect.left = WIDTH

        elif keys[pygame.K_RIGHT]:
            self.rect.x += 5
            if self.rect.left > WIDTH:
                self.rect.right = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

