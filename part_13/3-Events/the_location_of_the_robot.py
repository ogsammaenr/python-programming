import pygame
import random

pygame.init()
window = pygame.display.set_mode((640, 480))
# sebebini bilmiyorum ama kendi bilgisayarimda .png dosyasi kullanamiyorum
# o yuzden .bmp formatina cevirdim
robot = pygame.image.load("robot.bmp")

# robotun genisligi ve uzunlugu
width = robot.get_width()
height = robot.get_height()

# ekranin merkezinde baslatiyoruz
x = 320 - width / 2
y = 240 - height / 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_x, click_y = event.pos

            # tiklanan nokta robotun uzerinde mi
            if x <= click_x <= x + width and y <= click_y <= y + height:
                # ekrandan tasmayacak sekilde bir rastgele konum olusturuyoruz
                x = random.randint(0, 640 - width)
                y = random.randint(0, 480 - height)

        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()
