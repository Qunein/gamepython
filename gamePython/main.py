import pygame
import random

# Инициализация Pygame
pygame.init()

# Определение констант
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
METEOR_WIDTH = 50
METEOR_HEIGHT = 50

# Создание игрового окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("game")

# Загрузка изображения корабля и изменение его размера
player_img = pygame.image.load('cosmo.png')
player_img = pygame.transform.scale(player_img, (PLAYER_WIDTH, PLAYER_HEIGHT))

# Загрузка изображения метеорита и изменение его размера
meteor_img = pygame.image.load('i.png')
meteor_img = pygame.transform.scale(meteor_img, (METEOR_WIDTH, METEOR_HEIGHT))

# Класс для игрока (космического корабля)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 20
        self.speed_x = 0

    def update(self):
        self.rect.x += self.speed_x
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

# Класс для метеоритов
class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = meteor_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - METEOR_WIDTH)
        self.rect.y = random.randrange(-100, -METEOR_HEIGHT)
        self.speed_y = random.randrange(3, 10)  # Увеличиваем диапазон скорости метеоритов

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > SCREEN_HEIGHT + 10:
            self.rect.x = random.randrange(SCREEN_WIDTH - METEOR_WIDTH)
            self.rect.y = random.randrange(-100, -METEOR_HEIGHT)
            self.speed_y = random.randrange(3, 10)  # Увеличиваем диапазон скорости метеоритов

# Создание групп спрайтов
all_sprites = pygame.sprite.Group()
meteors = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Создание метеоритов
for i in range(8):
    meteor = Meteor()
    all_sprites.add(meteor)
    meteors.add(meteor)

# Создание основного игрового цикла
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.speed_x = -5
            elif event.key == pygame.K_RIGHT:
                player.speed_x = 5
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.speed_x = 0

    all_sprites.update()

    hits = pygame.sprite.spritecollide(player, meteors, False)
    if hits:
        running = False

    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
