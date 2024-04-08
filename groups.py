import random

import pygame

from settings import GAME_COLORS
from block import Block


class BlockGroup(pygame.sprite.Group):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.matrix = [None for i in range(width * height)]

    def __repr__(self):
        return f"BlockGroup <({self.width}, {self.height})>"

    def randomize(self):
        for i in range(self.height):
            for j in range(self.width):
                color = random.choice(GAME_COLORS)
                block = Block(self, j, i, color)
                self.add_block_to_position(block, j, i)

    def get_block_by_position(self, x, y):
        return self.matrix[x + y * self.width]

    def remove_block_for_position(self, x, y):
        block = self.get_block_by_position(x, y)
        block.kill()
        # self.matrix[x + y * self.width] = None

    def remove_blocks_by_position_list(self, position_list):
        for x, y in position_list:
            self.remove_block_for_position(x, y)

    def add_block_to_position(self, block, x, y):
        if self.matrix[x + y * self.width] is None:
            self.matrix[x + y * self.width] = block
        else:
            raise Exception(
                f"Already has a block in this position: ({x}, {y})"
            )

    def has_block(self, x, y):
        if self.matrix[x + y * self.width] is None:
            return False
        else:
            return True
