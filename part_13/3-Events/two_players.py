import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))
# sebebini bilmiyorum ama kendi bilgisayarimda .png dosyasi kullanamiyorum
# o yuzden .bmp formatina cevirdim
robot = pygame.image.load("robot.bmp")

# robotun genisligi ve uzunlugu
width = robot.get_width()
height = robot.get_height()

# birinci oyuncu (ok tuslari)
p1_x, p1_y = 150, 240
p1_left = p1_right = p1_up = p1_down = False

# ikinci oyuncu (waasd tuslari)
p2_x, p2_y = 450, 240
p2_left = p2_right = p2_up = p2_down = False

clock = pygame.time.Clock()

# bu soruda dokumanda anlatilan yontem ile cozdum
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            # Oyuncu 1
            if event.key == pygame.K_LEFT:
                p1_left = True
            if event.key == pygame.K_RIGHT:
                p1_right = True
            if event.key == pygame.K_UP:
                p1_up = True
            if event.key == pygame.K_DOWN:
                p1_down = True

            # Oyuncu 2
            if event.key == pygame.K_a:
                p2_left = True
            if event.key == pygame.K_d:
                p2_right = True
            if event.key == pygame.K_w:
                p2_up = True
            if event.key == pygame.K_s:
                p2_down = True

        if event.type == pygame.KEYUP:
            # Oyuncu 1
            if event.key == pygame.K_LEFT:
                p1_left = False
            if event.key == pygame.K_RIGHT:
                p1_right = False
            if event.key == pygame.K_UP:
                p1_up = False
            if event.key == pygame.K_DOWN:
                p1_down = False

            # Oyuncu 2
            if event.key == pygame.K_a:
                p2_left = False
            if event.key == pygame.K_d:
                p2_right = False
            if event.key == pygame.K_w:
                p2_up = False
            if event.key == pygame.K_s:
                p2_down = False

        if event.type == pygame.QUIT:
            exit()

    # Pozisyonları güncelle
    if p1_left:
        p1_x -= 3
    if p1_right:
        p1_x += 3
    if p1_up:
        p1_y -= 3
    if p1_down:
        p1_y += 3

    if p2_left:
        p2_x -= 3
    if p2_right:
        p2_x += 3
    if p2_up:
        p2_y -= 3
    if p2_down:
        p2_y += 3

    if p1_x < 0:
        p1_x = 0
    if p1_x > 640 - width:
        p1_x = 640 - width
    if p1_y < 0:
        p1_y = 0
    if p1_y > 480 - height:
        p1_y = 480 - height

    if p2_x < 0:
        p2_x = 0
    if p2_x > 640 - width:
        p2_x = 640 - width
    if p2_y < 0:
        p2_y = 0
    if p2_y > 480 - height:
        p2_y = 480 - height

    window.fill((0, 0, 0))
    window.blit(robot, (p1_x, p1_y))
    window.blit(robot, (p2_x, p2_y))
    pygame.display.flip()

    clock.tick(60)
