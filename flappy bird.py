#Flappy Bird

import pygame
import time
import random
pygame.init()

screen = pygame.display.set_mode((400,400))


def close():
    pygame.quit()
    quit()


pos = [100, 300]
vel = [0, -15]
acc = [0, 1]

walls = []
counter = 0
gap = 200

while True:
    # GAME LOOP
    screen.fill([0, 0, 0])
    if pos[1] >= 400 - 30:
        pos[1] = 400 - 30

    if counter % 50 == 0:
        walls.append([400, random.randint(0, 400 - gap)])
        if len(walls) >= 4:
            walls.pop(0)

    for wall in walls:
        x = wall[0]
        y = wall[1]
        pygame.draw.rect(screen, [255, 0, 0], [x, 0, 10, y])
        pygame.draw.rect(screen, [255, 0, 0], [x, y + gap, 10, 400 - gap - y])

        wall[0] -= 4

    pygame.draw.rect(screen, [255, 255, 255], [pos[0], pos[1], 10, 30])
    pos[0] += vel[0]
    pos[1] += vel[1]
    vel[0] += acc[0]
    vel[1] += acc[1]

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                close()
            elif event.key == pygame.K_SPACE:
                vel[1] = -15
        if event.type == pygame.QUIT:
            close()

    time.sleep(0.02)
    counter += 1

close()