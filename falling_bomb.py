import os

import pygame

from config import Config
from ship import Ship

is_falling = []


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
        self.size = Config.BOMB_SIZE
        self.falling_speed = Config.BOMB_FALLING_SPEED
        self.moving_speed_x = abs(self.finish_x - self.x) / ((self.size - Config.CEIL_HEIGHT) / self.falling_speed)
        self.moving_speed_y = abs(self.finish_y - self.y) / ((self.size - Config.CEIL_HEIGHT) / self.falling_speed)
        self.file_path = os.path.join('.', 'static', 'img', 'falling_bomb.png')
        self.burst_x = self.finish_x - Config.CEIL_HEIGHT // 3
        self.burst_y = self.finish_y - Config.CEIL_HEIGHT // 3
        self.burst_field = field
        self.burst_timer = 0
        self.burst_frames_number = len(os.listdir(os.path.join('.', 'static', 'img', 'burst')))
        self.burst_frames_path = [os.path.join('.', 'static', 'img', 'burst', f'{i}.png')
                                  for i in range(self.burst_frames_number)]
        self.burst_frames = [pygame.transform.scale(pygame.image.load(self.burst_frames_path[i]),
                                                    (Config.CEIL_HEIGHT * 1.75, Config.CEIL_HEIGHT * 1.75))
                             for i in range(self.burst_frames_number)]
        self.sprite = pygame.image.load(self.file_path)
        is_falling.append((self, self.field))
        self.fall()

    def fall(self):
        global is_falling
        self.x += self.moving_speed_x * (self.x < self.finish_x)
        self.x -= self.moving_speed_x * (self.x > self.finish_x)
        self.y += self.moving_speed_y * (self.y < self.finish_y)
        self.y -= self.moving_speed_y * (self.y > self.finish_y)
        if self.size > Config.CEIL_HEIGHT:
            self.size -= self.falling_speed
            self.sprite = pygame.transform.scale(self.sprite, (self.size, self.size))
        else:
            self.sprite = self.burst_frames[self.burst_timer]
            self.x = self.burst_x
            self.y = self.burst_y
            self.burst_timer += 1
            if self.burst_timer >= self.burst_frames_number:
                is_falling.remove((self, self.field))
            if self.field.field_ships[self.ceil_x][self.ceil_y] is not Ship:
                (self.field.field_ships[self.ceil_x][self.ceil_y]).shot(self.ceil_x, self.ceil_y)
            else:
                self.field.field_view[self.ceil_x][self.ceil_y] = 4
