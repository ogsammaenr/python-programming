import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))
# sebebini bilmiyorum ama kendi bilgisayarimda .png dosyasi kullanamiyorum
# o yuzden .bmp formatina cevirdim
robot = pygame.image.load("robot.bmp")

# mouseinin gorunumunu kapatiyoruz
pygame.mouse.set_visible(False)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # mousenin koordinatlarini aliyoruz
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # robotu mousenin merkezine aliyoruz
    x = mouse_x - robot.get_width() / 2
    y = mouse_y - robot.get_height() / 2

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()
