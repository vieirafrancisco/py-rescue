import random

import pygame

from settings import *
from matrix import Matrix
from graph import Graph

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# matrix
grid = True
matrix = Matrix(COLUMNS, ROWS)
matrix.randomize()

# groups
blocks_group = pygame.sprite.Group()
blocks_group.add(tuple(matrix.blocks))

# graph
graph = Graph()

## add nodes
for block in matrix.blocks:
    graph.add_node(block.pos)

## create edges
for block in matrix.blocks:
    x, y = block.pos
    directions = filter(
        lambda pos: 0 <= pos[0] < COLUMNS and 0 <= pos[1] < ROWS,
        [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]
    )
    for ax, ay in directions:
        adjacent_block = matrix.get_block_by_position(ax, ay)
        if adjacent_block.color == block.color:
            graph.create_edge(block.pos, adjacent_block.pos)
print(graph.graph)

def draw_grid():
    if grid:
        for x in range(0, WIDTH, TILE_SIZE):
            pygame.draw.line(screen, GRAY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILE_SIZE):
            pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y))

def render():
    # draw random square colors
    blocks_group.draw(screen)
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