import pygame

from settings import *

class Block(pygame.sprite.Sprite):
    def __init__(self, group, x, y, color):
        self.group = group
        pygame.sprite.Sprite.__init__(self, group)
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft = (x * TILE_SIZE, y * TILE_SIZE))
        self.gravity = -2
        self.x = x
        self.y = y
        self.color = color

    def __repr__(self):
        return f"Block <{self.color}>"

    def update(self):
        if self.rect.bottomright[1] < HEIGHT:
            self.rect.y -= self.gravity
            self.y = self.rect.y // TILE_SIZE

    @property
    def pos(self):
        return self.x, self.y

    @property
    def px_pos(self):
        return self.x * TILE_SIZE, self.y * TILE_SIZE

    def kill(self):
        # wrapper para fazer alterações na matrix e no graph
        super().kill()