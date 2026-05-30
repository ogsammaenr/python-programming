import pygame
import math

pygame.init()
window = pygame.display.set_mode((640, 480))
# sebebini bilmiyorum ama kendi bilgisayarimda .png dosyasi kullanamiyorum
# o yuzden .bmp formatina cevirdim
robot = pygame.image.load("robot.bmp")

# robotun genisligi ve uzunlugu
width = robot.get_width() - 10
height = robot.get_height()

clock = pygame.time.Clock()

angle = 0
while True:
    # her seferinde ekrana yazdiriyoruz
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    for i in range(10):
        # 2 x pi = 360
        # 360 / 10 = 36
        # her robot arasinda 36 derece bosluk var ( i * 36 )
        # buna angle'i buna ekleyince butun sistem angle degiskenine bagli olmus oluyor
        current_angle = angle + (i * 2 * math.pi / 10)

        # cos(x) * 120 = yaricapi 120 olan cember uzerindeki x acisi ile cember uzerindeki noktanin x koordinatini verir
        # sin(x) * 120 = yaricapi 120 olan cember uzerindeki x acisi ile cember uzerindeki noktanin y koordinatini verir
        # en sondaki width / 2 | height / 2 robotlari cembere tam merkezinden cemver uzerine yerlestirmek icin
        # + 320 | + 240 ise cemberin merkezini uygulamanin merkezine hizalamak icin
        x = math.cos(current_angle) * 120 - width / 2 + 320
        y = math.sin(current_angle) * 120 - height / 2 + 240

        window.blit(robot, (x, y))

    pygame.display.flip()

    # cemberi 0.005 derece pozitif yonde donduruyoruz
    angle += 0.005
    clock.tick(144)
