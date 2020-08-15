import random

import pygame

# Constants
##############################################################################

## window
WIDTH, HEIGHT = 640, 480
FPS = 60

## colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
COLORS = [WHITE, BLACK, RED, GREEN, BLUE]

## game
TILE_SIZE = 32

##############################################################################

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
grid = True

def render():
    if grid:
        for x in range(0, WIDTH, TILE_SIZE):
            pygame.draw.line(screen, WHITE, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILE_SIZE):
            pygame.draw.line(screen, WHITE, (0, y), (WIDTH, y))
    # draw random square colors

    

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