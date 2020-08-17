import random

from settings import *
from block import Block

class Matrix:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.blocks = []

    def __repr__(self):
        return f"Matrix <({self.width}, {self.height})>"

    def randomize(self):
        for i in range(self.height):
            for j in range(self.width):
                color = random.choice(GAME_COLORS)
                block = Block(j, i, color)
                self.blocks.append(block)

    def get_block_by_position(self, x, y):
        return self.blocks[x + y * self.width]
