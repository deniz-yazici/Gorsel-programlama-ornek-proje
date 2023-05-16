import pygame
import random

# Oyun ekranı boyutları
WIDTH = 800
HEIGHT = 600

# Renkler
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Oyuncu sınıfı
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 50)
    
    def update(self):
        # Klavye girişlerini kontrol et
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

        # Oyuncunun oyun alanı dışına çıkmasını engelle
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

# Düşman sınıfı
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 4)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 4)

# Pygame başlatma
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basit Oyun")
clock = pygame.time.Clock()

# Oyuncu ve düşman grupları
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Düşmanları oluştur
for _ in range(10):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

# Oyun döngüsü
running = True
while running:
    # Oyun hızı
    clock.tick(60)

    # Kapatma işlemi
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Oyuncu ve düşmanları güncelle
    all_sprites.update()

    # Çarpışma kontrolü
    hits = pygame.sprite.spritecollide(player, enemies, False)
    if hits:
        running = False

    # Ekranı temizle ve nesneleri çiz
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

# Oyun döngüsünden çıkıldığında Pygame'i kapat
pygame.quit()
