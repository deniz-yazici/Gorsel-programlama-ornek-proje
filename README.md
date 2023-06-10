# Gorsel-programlama-ornek-proje
Görsel Programlama ile örnek oyun veya projeler için fikir oluşturacaktır.

Gerekli Araçları Kurma:

Bilgisayarınıza Python programlama dilini indirin ve kurun. Python'un resmi web sitesinden indirebilirsiniz.
Pygame kütüphanesini yüklemek için komut istemcisini açın ve pip install pygame komutunu çalıştırın.

Proje Dizinini Hazırlama:
Bir proje dizini oluşturun ve bu dizine geçin.
Bu dizinde Python kodunu içerecek bir dosya oluşturun. Örneğin, oyun.py olarak adlandırabilirsiniz.

Python Kodunun Yazılması:
Metin düzenleyici veya Python geliştirme ortamı (IDE) kullanarak oyun.py dosyasını açın.
Önce, gerekli modülleri ve renkleri tanımlayalım:

import pygame
import random

WIDTH = 800
HEIGHT = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

Oyuncu ve düşman sınıflarını tanımlayalım:

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 50)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
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
            
Pygame'in başlatılması ve oyun ekranının oluşturulması:

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basit Oyun")
clock = pygame.time.Clock()

Oyuncu ve düşman gruplarının oluşturulması:

all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

for _ in range(8):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)
    
Oyun döngüsünün tanımlanması ve ana oyun döngüsünün oluşturulması:

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    hits = pygame.sprite.spritecollide(player, enemies, False)
    if hits:
        running = False

    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()

Oyunun Çalıştırılması:
Komut istemcisini açın ve proje dizinine geçin.
python oyun.py komutunu çalıştırarak oyunu başlatın.
Oyuncu karakteri sol ve sağ ok tuşlarıyla hareket ettirilebilir. Amacınız düşman karakterlere çarpmadan mümkün olduğunca uzun süre hayatta kalmaktır.

Bu adımları takip ederek, basit bir görsel oyunu Python kullanarak oluşturabilir ve çalıştırabiliriz. Bu örneği genişletebilir ve oyunu daha karmaşık hale getirebiliriz, örneğin, puanlama sistemi, ses efektleri, daha fazla düşman veya ek özellikler ekleyebiliriz.
