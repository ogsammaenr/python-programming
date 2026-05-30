import pygame
import random

pygame.init()
window = pygame.display.set_mode((640, 480))
# sebebini bilmiyorum ama kendi bilgisayarimda .png dosyasi kullanamiyorum
# o yuzden .bmp formatina cevirdim
robot = pygame.image.load("robot.bmp")

width = robot.get_width()
height = robot.get_height()

# ekrandaki robotlarin listesi
robots = []

clock = pygame.time.Clock()
while True:
    window.fill((0, 0, 0))

    # %2 sansla gokten robot yagmasini sagliyoruz
    # her tickte calisiyor yani saniyede 144 kere
    if random.randint(1, 50) == 1:
        robots.append(
            {
                "x": random.randint(0, 640 - robot.get_width()),
                "y": -height,
                "vel_x": 0,
                "vel_y": random.randint(1, 5),
            }
        )

    # listedeki butun robotlar icin islem yapiyoruz
    for r in robots:
        # ilerletiyoruz
        r["x"] += r["vel_x"]
        r["y"] += r["vel_y"]

        # yere carpma kontrolu
        if r["y"] + height >= 480 and r["vel_y"] > 0:
            # yere carptiysa dusmesini engelliyoruz
            r["vel_y"] = 0
            # rastege bir yone dogru ( sag veya sol ) gitmesini sagliyoruz
            r["vel_x"] = random.choice([-2, 2])

        window.blit(robot, (r["x"], r["y"]))

        # ekrandan cikan robotlari siliyoruz
        if r["x"] < -100 or r["x"] > 740:
            robots.remove(r)

    pygame.display.flip()
    clock.tick(144)
    # her seferinde ekrana yazdiriyoruz
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
