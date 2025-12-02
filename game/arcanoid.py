import pygame
import random
from game import WIDTH, HEIGHT, WHITE, GREEN,FPS,BLACK, RED, Player, Ball, Bricks
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arcanoid")
clock = pygame.time.Clock()

def show_go_screen():
    screen.blit(background, background_rect)
    draw_text(screen, f"Your score:{score}", 20, WIDTH / 2-20, HEIGHT * 3 / 4-30)
    draw_text(screen, "Press <Space> to begin", 20, WIDTH / 2, HEIGHT * 3 / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                waiting = False
            if event.type == pygame.KEYUP:
                waiting = False

font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

background = pygame.Surface(screen.get_size())
background.fill((0, 0, 0))
background_rect = background.get_rect()

#игрок
player_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
player_group.add(player)
#мяч
ball = Ball()
all_sprites.add(ball)
#кирпич
bricks_group = pygame.sprite.Group()
for a in range(0,17):
    for b in range(2,11):
        x=1+41*a
        y=1+16*b
        brick = Bricks(x,y)
        all_sprites.add(brick)
        bricks_group.add(brick)
score = 0
# Цикл игры
game_over = False
running = True

while running:
    clock.tick(FPS)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if keys[pygame.K_SPACE]:
            waiting = False
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
    if ball.rect.top> HEIGHT:
        game_over = True
    if game_over:
        show_go_screen()
        game_over = False
        all_sprites = pygame.sprite.Group()
        bricks_group = pygame.sprite.Group()
        for a in range(0, 17):
            for b in range(2, 11):
                x = 1 + 41 * a
                y = 1 + 16 * b
                brick = Bricks(x, y)
                all_sprites.add(brick)
                bricks_group.add(brick)
        ball = Ball()
        all_sprites.add(ball)
        player = Player()
        all_sprites.add(player)
        score = 0
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    all_sprites.update()

    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    draw_text(screen, str(score), 20, WIDTH / 2, 10)
    if score==0:
        draw_text(screen, "Press <Space> to begin", 20, WIDTH / 2, HEIGHT * 3 / 4)

    pygame.display.flip()
pygame.quit()