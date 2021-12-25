from config import Config

import os

import pygame


class Burst:
    def __init__(self, x, y, field):
        self.x = x - 20
        self.y = y - 20
        self.field = field
        self.timer = 0
        self.frames_path = [os.path.join('.', 'static', 'img', 'burst', f'{i}.png') for i in range(20)]
        self.frames = [pygame.transform.scale(pygame.image.load(self.frames_path[i]),
                                              (Config.CEIL_HEIGHT + 53, Config.CEIL_HEIGHT + 53)) for i in range(20)]
        # self.file_path = os.path.join('.', 'static', 'img', 'burst.gif')
        # self.sprite = pygame.image.load(self.file_path)
        # self.sprite = pygame.transform.scale(self.sprite, (Config.CEIL_HEIGHT, Config.CEIL_HEIGHT))
