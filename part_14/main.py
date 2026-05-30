import pygame
import sys
import os

from player import Player
from pipes import PipePair

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Pygame Kurulumu
pygame.init()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 900
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

print(pygame.image.get_sdl_image_version())

# Arka planı yüklüyoruz
bg_path = os.path.join(BASE_DIR, "assets", "background.png")
bg_surface = pygame.image.load(bg_path).convert()
bg_surface = pygame.transform.scale(bg_surface, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Nesnelerin Örneklenmesi (Instantiation)
player = Player(100, SCREEN_HEIGHT // 2)
pipes = []

# Boru üretmek için Custom Event
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)

game_active = True


def check_collision(player, pipes):
    for pipe in pipes:
        # colliderect iki dortgenin cakisip cakismadigini kontrol eder
        if player.rect.colliderect(pipe.bottom_rect) or player.rect.colliderect(
            pipe.top_rect
        ):
            return False
    # oyuncunun collider'inin yere veya tepeye carpip carpmadigini kontrol ediyoruz
    if player.rect.top <= 0 or player.rect.bottom >= SCREEN_HEIGHT:
        return False
    return True


# Ana Oyun Döngüsü
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                player.jump()
            if event.key == pygame.K_SPACE and not game_active:
                # Oyunu Yeniden Başlat (Reset)
                player = Player(100, SCREEN_HEIGHT // 2)
                pipes.clear()
                game_active = True

        if event.type == SPAWNPIPE and game_active:
            # Yeni bir boru çifti ekle (Ekranın hemen sağından başlayacak şekilde)
            pipes.append(PipePair(SCREEN_WIDTH + 100, SCREEN_HEIGHT))

    # 1. Arka planı çiz
    screen.blit(bg_surface, (0, 0))

    if game_active:
        # 2. Güncellemeleri yap (Fizik ve Pozisyonlar)
        player.update()

        for pipe in pipes:
            pipe.update()

        # Ekrandan çıkan boruları temizle (Bellek optimizasyonu)
        pipes = [pipe for pipe in pipes if not pipe.is_offscreen()]

        # 3. Çarpışma Kontrolü
        game_active = check_collision(player, pipes)

    # 4. Ekrana Çizimler
    for pipe in pipes:
        pipe.draw(screen)

    player.draw(screen)

    pygame.display.update()
    clock.tick(60)

# Bu oyun yapay zeka yardimi ile olusturulmustur
