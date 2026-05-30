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
x = 0
y = 0

# x eksenindeki hareket hizi
x_vel = 1
# y eksenindeki hareket hizi
y_vel = 0

# genel hiz carpani
velocity = 2

clock = pygame.time.Clock()
while True:
    # her seferinde ekrana yazdiriyoruz
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    y += y_vel * velocity
    x += x_vel * velocity

    # alt kenera carptiginda sola ceviriyoruz
    if y_vel > 0 and y + height >= 480:
        y_vel = 0
        x_vel = -1
    # ust kenera carptiginda saga ceviriyoruz
    if y_vel < 0 and y <= 0:
        y_vel = 0
        x_vel = 1
    # sag kenera carptiginda asagiya ceviriyoruz
    if x_vel > 0 and x + width >= 640:
        x_vel = 0
        y_vel = 1
    # sol kenera carptiginda yukari ceviriyoruz
    if x_vel < 0 and x <= 0:
        x_vel = 0
        y_vel = -1

    clock.tick(144)
