import pygame
import random


from game import WIDTH, HEIGHT, WHITE

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((15, 15), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.radius=int(self.rect.width/2)
        pygame.draw.circle(self.image,WHITE,(self.radius,self.radius),self.radius)
        self.rect.center = (WIDTH / 2, HEIGHT - self.rect.height-25)
        self.speed_x = 0
        self.speed_y = 0



    def update(self):
        keys = pygame.key.get_pressed()
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.speed_y == 0:
            if keys[pygame.K_SPACE]:
                self.speed_y = -5
                self.speed_x = -2

        if self.rect.left < 0:
            self.speed_x *= -1
        elif self.rect.right > WIDTH:
            self.speed_x *= -1
        elif self.rect.top < 0:
            self.speed_y *= -1






