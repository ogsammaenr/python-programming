import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))
# sebebini bilmiyorum ama kendi bilgisayarimda .png dosyasi kullanamiyorum
# o yuzden .bmp formatina cevirdim
robot = pygame.image.load("robot.bmp")

x = 100
y = 100

vel_x = 3
vel_y = 3

width = robot.get_width()
height = robot.get_height()

clock = pygame.time.Clock()
while True:
    x += vel_x
    y += vel_y

    # sol - sag duvak kontrolleri
    if x + width >= 640 or x <= 0:
        vel_x = -vel_x
    # ust - alt taban kontrolleri
    if y + height >= 480 or y <= 0:
        vel_y = -vel_y

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))

    pygame.display.flip()

    clock.tick(144)
    # her seferinde ekrana yazdiriyoruz
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
