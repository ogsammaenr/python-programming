import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))
# sebebini bilmiyorum ama kendi bilgisayarimda .png dosyasi kullanamiyorum
# o yuzden .bmp formatina cevirdim
robot = pygame.image.load("robot.bmp")

# robotun genisligi ve uzunlugu
width = robot.get_width() - 10
height = robot.get_height()

# koordinatlar
x1 = 0
y1 = 100

x2 = 0
y2 = 250

# hizlar
vel1 = 2

vel2 = 4


# genel hiz carpani
velocity = 2

clock = pygame.time.Clock()
while True:
    # her seferinde ekrana yazdiriyoruz
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    # 1. robot
    x1 += vel1
    if x1 + width >= 640 or x1 <= 0:
        vel1 = -vel1
    # 2. robot
    x2 += vel2
    if x2 + width >= 640 or x2 <= 0:
        vel2 = -vel2

    window.fill((0, 0, 0))
    window.blit(robot, (x1, y1))
    window.blit(robot, (x2, y2))
    pygame.display.flip()

    clock.tick(144)
