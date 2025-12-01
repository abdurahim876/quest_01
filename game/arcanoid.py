import pygame
import random

WIDTH = 700
HEIGHT = 500
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arcanoid")
clock = pygame.time.Clock()

font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)
background = pygame.Surface(screen.get_size())
background.fill((0, 0, 0))  # Например, черный фон
background_rect = background.get_rect()

#игрок
player_group = pygame.sprite.Group()
class Player(pygame.sprite.Sprite):
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

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
player_group.add(player)
#мяч
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((15, 15), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.radius=int(self.rect.width/2)
        pygame.draw.circle(self.image,WHITE,(self.radius,self.radius),self.radius)
        self.rect.center = (WIDTH / 2, HEIGHT - self.rect.height-25)

        self.speed_y = 5
        self.speed_x = 1


    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.left < 0:
            self.speed_x *= -1
        elif self.rect.right > WIDTH:
            self.speed_x *= -1
        elif self.rect.top < 0:
            self.speed_y *= -1
        elif self.rect.bottom > HEIGHT:
            self.speed_y *= -1
            self.rect.top = 15
            self.rect.center = (WIDTH / 2, HEIGHT - self.rect.height-25)
ball = Ball()
all_sprites.add(ball)

#кирпич
bricks_group = pygame.sprite.Group()
class Bricks(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40, 15))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x =x
        self.rect.y =y
for a in range(0,17):
    for b in range(2,11):
        x=1+41*a
        y=1+16*b
        brick = Bricks(x,y)
        all_sprites.add(brick)
        bricks_group.add(brick)
score = 0


# Цикл игры
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    all_sprites.update()

    hits = pygame.sprite.spritecollide(ball, bricks_group, True, pygame.sprite.collide_circle)
    if hits:
        ball.speed_y *= -1
        for hit in hits:
            score += 1
            brick = Bricks(x, y)
            all_sprites.add(brick)
            bricks_group.add(brick)

    hits = pygame.sprite.spritecollide(ball, player_group, False)
    if hits:
        ball.speed_y *= -1

    # Рендеринг
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    draw_text(screen, str(score), 20, WIDTH / 2, 10)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()