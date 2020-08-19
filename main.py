import random

import pygame

from settings import *
from groups import BlockGroup
from graph import GraphControl

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# variables
grid = False

# block_group
block_group = BlockGroup(COLUMNS, ROWS)
block_group.randomize()

# graph
gc = GraphControl()
gc.update(block_group)

def draw_grid():
    if grid:
        for x in range(0, WIDTH, TILE_SIZE):
            pygame.draw.line(screen, GRAY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILE_SIZE):
            pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y))

def render():
    # draw random square colors
    block_group.draw(screen)
    # grid
    draw_grid()
    # show fps
    pygame.display.set_caption(f"FPS: {round(clock.get_fps(), 2)}")
    

def update():
    mouse_click = pygame.mouse.get_pressed()
    if mouse_click[0]:
        mouse_pos = pygame.mouse.get_pos()
        mx = mouse_pos[0] // TILE_SIZE
        my = mouse_pos[1] // TILE_SIZE
        positions = gc.event_update(mx, my)
        if positions:
            block_group.remove_blocks_by_position_list(positions)
            gc.update(block_group)
    block_group.update()

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