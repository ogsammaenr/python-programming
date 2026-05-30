import pygame
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class Player:
    def __init__(self, x, y):
        # Sprite Sheet yükleme ve parçalama
        self.sprite_sheet = pygame.image.load(
            os.path.join(BASE_DIR, "assets", "bird_spritesheet.png")
        ).convert_alpha()

        self.frame_width = 16
        self.frame_height = 16
        self.total_frames = 4
        self.frames = []

        BUYUTME_KATSAYISI = 2

        for i in range(self.total_frames):
            kutu = pygame.Rect(
                i * self.frame_width, 0, self.frame_width, self.frame_height
            )
            kare_gorseli = self.sprite_sheet.subsurface(kutu)

            buyutulmus_kare = pygame.transform.scale_by(kare_gorseli, BUYUTME_KATSAYISI)

            self.frames.append(buyutulmus_kare)

        self.current_frame = 0
        self.animation_speed = 0.15

        # Fizik ve Konum değişkenleri
        self.image = self.frames[int(self.current_frame)]
        self.rect = self.image.get_rect(center=(x, y))
        self.gravity = 0.40
        self.movement = 0

    def jump(self):
        self.movement = 0
        self.movement -= 7

    def update(self):
        # Yerçekimi uygulaması
        self.movement += self.gravity
        self.rect.centery += self.movement

        # Animasyonu ilerletme
        self.current_frame += self.animation_speed
        if self.current_frame >= self.total_frames:
            self.current_frame = 0
        self.image = self.frames[int(self.current_frame)]

    def draw(self, screen):
        screen.blit(self.image, self.rect)
