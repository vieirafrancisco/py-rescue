import pygame

from settings import *

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft = (x * TILE_SIZE, y * TILE_SIZE))
        self.x = x
        self.y = y
        self.color = color

    def __repr__(self):
        return f"Block <{self.color}>"

    @property
    def pos(self):
        return self.x, self.y

    @property
    def px_pos(self):
        return self.x * TILE_SIZE, self.y * TILE_SIZE