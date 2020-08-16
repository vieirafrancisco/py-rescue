import pygame

from settings import *

class Block:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def __repr__(self):
        return f"Block <{self.color}>"

    def __eq__(self, other):
        if self.color == other.color:
            return True
        return False

    def draw(self, surface):
        px, py = self.px_pos
        pygame.draw.rect(surface, self.color, (px, py, TILE_SIZE, TILE_SIZE))

    @property
    def pos(self):
        return self.x, self.y

    @property
    def px_pos(self):
        return self.x * TILE_SIZE, self.y * TILE_SIZE