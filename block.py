import pygame

from settings import *

class Block:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def __repr__(self):
        return f"Block <{self.color}>"

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, TILE_SIZE, TILE_SIZE))