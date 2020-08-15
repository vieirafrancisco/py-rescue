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
GRAY = (75, 75, 75)
RED = (255,0,0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

## game
TILE_SIZE = 32
T_WIDTH = WIDTH // TILE_SIZE
T_HEIGHT = HEIGHT // TILE_SIZE
GAME_COLORS = [RED, GREEN, BLUE]

##############################################################################

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

## game
grid = True
matrix = []
# store random square colors
for x in range(0, WIDTH, TILE_SIZE):
    for y in range(0, HEIGHT, TILE_SIZE):
        color = random.choice(GAME_COLORS)
        matrix.append((screen, color, (x, y, TILE_SIZE, TILE_SIZE)))

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
            pygame.draw.rect(*matrix[i + j * T_WIDTH])

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