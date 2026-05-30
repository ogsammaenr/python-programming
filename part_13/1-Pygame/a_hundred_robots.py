import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))
# sebebini bilmiyorum ama kendi bilgisayarimda .png dosyasi kullanamiyorum
# o yuzden .bmp formatina cevirdim
robot = pygame.image.load("robot.bmp")

# robotun genisligi ve uzunlugu
width = robot.get_width() - 10
height = robot.get_height()

window.fill((0, 0, 0))

# 10 tane robot satiri
for row in range(10):
    # 10 tane yan yana robot
    for col in range(10):
        # izometrik goruntu icin her satiri biraz daha saga kaydiriyoruz
        x_pos = col * width + row * 10
        y_pos = row * 20
        # sol uste yapisik olmamasi icin 50 pixel bosluk birakiyoruz
        window.blit(robot, (x_pos + 50, y_pos + 50))

pygame.display.flip()

# pygame kapanis dongusu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
