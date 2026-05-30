import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))
# sebebini bilmiyorum ama kendi bilgisayarimda .png dosyasi kullanamiyorum
# o yuzden .bmp formatina cevirdim
robot = pygame.image.load("robot.bmp")

# robotun genisligi ve uzunlugu
width = robot.get_width()
height = robot.get_height()

window.fill((0, 0, 0))

# 10 kere x degerini arttirarak ekrana yazdiriyoruz
for i in range(10):
    x_pos = i * width
    y_pos = 100  # hepsi ayni hizada
    window.blit(robot, (x_pos + 50, y_pos))

pygame.display.flip()

# pygame kapanis dongusu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
