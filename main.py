import random

import pygame

from settings import *
from block import Block

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

## load stuff
grid = True
matrix = []
# store random square colors
for x in range(0, WIDTH, TILE_SIZE):
    for y in range(0, HEIGHT, TILE_SIZE):
        color = random.choice(GAME_COLORS)
        block = Block(x, y, color)
        matrix.append(block)

def draw_grid():
    if grid:
        for x in range(0, WIDTH, TILE_SIZE):
            pygame.draw.line(screen, GRAY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILE_SIZE):
            pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y))

def render():
    # draw random square colors
    for i in range(T_WIDTH):
        for j in range(T_HEIGHT):
            matrix[i + j * T_WIDTH].draw(screen)

    # grid
    draw_grid()
    

def update():
    ...

running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                grid = not grid
    screen.fill(BLACK)
    render()
    update()
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()