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

# sol ust
window.blit(robot, (0, 0))
# sag ust
window.blit(robot, (640 - width, 0))
# sol alt
window.blit(robot, (0, 480 - height))
# sag alt
window.blit(robot, (640 - width, 480 - height))

# oyunu ekrana yazdiriyoruz
pygame.display.flip()

# pygame kapanis dongusu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
