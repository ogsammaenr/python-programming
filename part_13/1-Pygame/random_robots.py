import pygame
import random

pygame.init()
window = pygame.display.set_mode((640, 480))
# sebebini bilmiyorum ama kendi bilgisayarimda .png dosyasi kullanamiyorum
# o yuzden .bmp formatina cevirdim
robot = pygame.image.load("robot.bmp")

# robotun genisligi ve uzunlugu
width = robot.get_width() - 10
height = robot.get_height()

window.fill((0, 0, 0))

# 1000 adet rastgele robot cizimi
for _ in range(1000):
    # tasmayi engellemek icin sinirlari robutun boyutlari kadar daraltiyoruz
    x_pos = random.randint(0, 640 - width)
    y_pos = random.randint(0, 480 - height)

    window.blit(robot, (x_pos, y_pos))

pygame.display.flip()

# pygame kapanis dongusu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
