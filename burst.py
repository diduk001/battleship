# TODO: add burst animation to falling bomb animation because Burst have only __init__ and this class in unnecessary
import os

import pygame

from config import Config


class Burst:
    def __init__(self, x, y, field):
        # TODO: get rid of constants ( -20, +53 )
        self.x = x - 20
        self.y = y - 20
        self.field = field
        self.timer = 0
        # TODO: automatically detect number of frames
        self.frames_path = [os.path.join('.', 'static', 'img', 'burst', f'{i}.png') for i in range(20)]
        self.frames = [pygame.transform.scale(pygame.image.load(self.frames_path[i]),
                                              (Config.CEIL_HEIGHT + 53, Config.CEIL_HEIGHT + 53)) for i in range(20)]
