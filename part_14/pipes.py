import pygame
import random
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class PipePair:
    def __init__(self, x, screen_height):
        self.original_pipe_surface = pygame.image.load(
            os.path.join(BASE_DIR, "assets", "pipe.png")
        ).convert_alpha()

        self.speed = 3
        self.gap = 150
        self.screen_height = screen_height
        self.pipe_width = 32

        # 1. Boruların yüksekliğini rastgele belirle
        # Üst borunun minimum 50, maksimum (ekran - boşluk - 50) yükseklikte olmasını sağlıyoruz
        self.top_height = random.randint(50, self.screen_height - self.gap - 50)
        self.bottom_height = self.screen_height - self.top_height - self.gap

        # 2. Görselleri dinamik olarak YÜKSEKLİĞE GÖRE ESNET (Scale)
        # Üst Boru: (Genişlik, Dinamik Üst Yükseklik) boyutuna esnet ve dikeyde ters çevir
        scaled_top = pygame.transform.scale(
            self.original_pipe_surface, (self.pipe_width, self.top_height)
        )
        self.top_image = pygame.transform.flip(scaled_top, False, True)

        # Alt Boru: (Genişlik, Dinamik Alt Yükseklik) boyutuna esnet
        self.bottom_image = pygame.transform.scale(
            self.original_pipe_surface, (self.pipe_width, self.bottom_height)
        )

        # 3. Dikdörtgenleri (Rect) konumlandır
        # Üst boru ekranın en tepesinden (y=0) başlar
        self.top_rect = self.top_image.get_rect(topleft=(x, 0))
        # Alt boru ekranın en altından (y=screen_height) yukarıya doğru hizalanır
        self.bottom_rect = self.bottom_image.get_rect(
            bottomleft=(x, self.screen_height)
        )

    def update(self):
        # Boruları sola kaydır
        self.bottom_rect.centerx -= self.speed
        self.top_rect.centerx -= self.speed

    def draw(self, screen):
        screen.blit(self.top_image, self.top_rect)
        screen.blit(self.bottom_image, self.bottom_rect)

    def is_offscreen(self):
        return self.bottom_rect.right < 0
