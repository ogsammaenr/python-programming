import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))
# sebebini bilmiyorum ama kendi bilgisayarimda .png dosyasi kullanamiyorum
# o yuzden .bmp formatina cevirdim
robot = pygame.image.load("robot.bmp")

# robotun genisligi ve uzunlugu
width = robot.get_width() - 10
height = robot.get_height()

x = 0
y = 0
# hareket hizi
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

    y += velocity

    # alt kenera carptiginda hizi ters ceviriyoruz
    if velocity > 0 and y + height >= 480:
        velocity = -velocity
    # ust kenera carptiginda hizi ters ceviriyoruz
    if velocity < 0 and y <= 0:
        velocity = -velocity

    clock.tick(60)
