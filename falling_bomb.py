from config import Config
from ship import Ship
from burst import Burst

import pygame

import os

is_falling = []
is_bursting = []


class FallingBomb:
    def __init__(self, x, y, field):
        global is_falling
        self.field = field
        self.finish_x = (x + 1) * self.field.border_weight + x * self.field.ceil_width
        self.finish_y = (y + 1) * self.field.border_weight + y * self.field.ceil_height
        self.ceil_x = x
        self.ceil_y = y
        self.x = 0
        self.y = 0
        self.falling_speed = 20
        self.size = 500
        self.moving_speed_x = abs(self.finish_x - self.x) / ((self.size - Config.CEIL_HEIGHT) / self.falling_speed)
        self.moving_speed_y = abs(self.finish_y - self.y) / ((self.size - Config.CEIL_HEIGHT) / self.falling_speed)
        self.file_path = os.path.join('.', 'static', 'img', 'falling_bomb.png')
        self.sprite = pygame.image.load(self.file_path)
        is_falling.append((self, self.field))
        self.fall()

    def fall(self):
        # log.info("bomb is falling")
        global is_falling
        self.x += self.moving_speed_x * (self.x < self.finish_x)
        self.x -= self.moving_speed_x * (self.x > self.finish_x)
        self.y += self.moving_speed_y * (self.y < self.finish_y)
        self.y -= self.moving_speed_y * (self.y > self.finish_y)
        if self.size > Config.CEIL_HEIGHT:
            self.size -= self.falling_speed
            self.sprite = pygame.transform.scale(self.sprite, (self.size, self.size))
        else:
            is_falling.remove((self, self.field))
            is_bursting.append(Burst(self.x, self.y, self.field))
            if self.field.field_ships[self.ceil_x][self.ceil_y] is not Ship:
                (self.field.field_ships[self.ceil_x][self.ceil_y]).shot(self.ceil_x, self.ceil_y)
            else:
                self.field.field_view[self.ceil_x][self.ceil_y] = 4