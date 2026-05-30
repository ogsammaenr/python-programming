import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))
# sebebini bilmiyorum ama kendi bilgisayarimda .png dosyasi kullanamiyorum
# o yuzden .bmp formatina cevirdim
robot = pygame.image.load("robot.bmp")

# robotun genisligi ve uzunlugu
width = robot.get_width()
height = robot.get_height()

# robotu ekranin merkezinde baslatiyoruz
x = 320 - robot.get_width() / 2
y = 240 - robot.get_height() / 2

# x ve y koordinatlarindaki hizlari
vel_x = 0
vel_y = 0

# genel hiz carpani
velocity = 5

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                vel_x = -1
            if event.key == pygame.K_RIGHT:
                vel_x = 1
            if event.key == pygame.K_UP:
                vel_y = -1
            if event.key == pygame.K_DOWN:
                vel_y = 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                vel_x = 0
            if event.key == pygame.K_RIGHT:
                vel_x = 0
            if event.key == pygame.K_UP:
                vel_y = 0
            if event.key == pygame.K_DOWN:
                vel_y = 0

        if event.type == pygame.QUIT:
            exit()

    # Koordinatları güncelleme
    x += vel_x * velocity
    y += vel_y * velocity

    if x < 0:
        x = 0
    if x > 640 - width:
        x = 640 - width
    if y < 0:
        y = 0
    if y > 480 - height:
        y = 480 - height

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    clock.tick(60)
