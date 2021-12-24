import os
import random

import pygame

from config import Config
from ship import Ship


class Field:
    def __init__(self) -> None:
        self.size = self.width, self.height = Config.FIELD_WIDTH, Config.FIELD_HEIGHT
        self.ceil_size = self.ceil_width, self.ceil_height = Config.CEIL_WIDTH, Config.CEIL_HEIGHT
        self.screen_size = self.screen_width, self.screen_height = Config.FIELD_PIX_WIDTH, Config.FIELD_PIX_HEIGHT

        self.border_weight = Config.BORDER_WEIGHT
        self.border_color = Config.BORDER_COLOR

        self._initialized = False
        self.field_view = [[0 for j in range(self.height)] for i in range(self.width)]
        self.field_ships = [[Ship for j in range(self.height)] for i in range(self.width)]
        self.free_spots = []
        for i in range(10):
            for j in range(10):
                self.free_spots.append((i, j))

        self.ships_sizes = Config.SHIPS_SIZES

        self.ceil_sprites = []
        for filename in Config.CEIL_SPRITES_FILENAMES:
            file_path = os.path.join('.', 'static', 'img', filename)
            file = pygame.image.load(file_path)
            self.ceil_sprites.append(file)

        self.build()

    @staticmethod
    def get_field_cords_by_screen_cords(surface_cords: tuple[int, int]) -> tuple[int, int]:
        screen_x, screen_y = surface_cords

        field_x = screen_x // (Config.CEIL_WIDTH + Config.BORDER_WEIGHT)
        if field_x >= Config.FIELD_WIDTH:
            field_x = Config.FIELD_WIDTH - 1

        field_y = screen_y // (Config.CEIL_HEIGHT + Config.BORDER_WEIGHT)
        if field_y >= Config.FIELD_HEIGHT:
            field_y = Config.FIELD_HEIGHT - 1

        return field_x, field_y

    def click(self, cords: tuple[int, int]) -> None:
        field_cords = self.get_field_cords_by_screen_cords(cords)
        self.shoot(field_cords)

    def shoot(self, field_cords: tuple[int, int]) -> None:
        x, y = field_cords
        if self.field_ships[x][y] is not Ship:
            (self.field_ships[x][y]).shot(x, y)
            self.field_view[x][y] = 5
        else:
            self.field_view[x][y] = 4

    def render(self, screen: pygame.Surface) -> None:
        assert self._initialized

        # draw grid from borders
        for col in range(self.width + 1):
            col_x = (self.border_weight + self.ceil_width) * col
            start_pos = (col_x, 0)
            end_pos = (col_x, self.screen_height)
            pygame.draw.line(screen, self.border_color, start_pos, end_pos, width=self.border_weight)
        # draw last border
        x_last_start_pos = (self.screen_width - self.border_weight, 0)
        x_last_end_pos = (self.screen_width - self.border_weight, self.screen_height)
        pygame.draw.line(screen, self.border_color, x_last_start_pos, x_last_end_pos, width=self.border_weight)

        for row in range(self.height + 1):
            row_y = (self.border_weight + self.ceil_height) * row
            start_pos = (0, row_y)
            end_pos = (self.screen_width, row_y)
            pygame.draw.line(screen, self.border_color, start_pos, end_pos, width=self.border_weight)

        y_last_start_pos = (0, self.screen_height - self.border_weight)
        y_last_end_pos = (self.screen_width, self.screen_height - self.border_weight)
        pygame.draw.line(screen, self.border_color, y_last_start_pos, y_last_end_pos, width=self.border_weight)

        for x in range(self.width):
            for y in range(self.height):
                ceil_type = self.field_view[x][y]
                ceil_sprite = self.ceil_sprites[ceil_type]
                left = (x + 1) * self.border_weight + x * self.ceil_width
                top = (y + 1) * self.border_weight + y * self.ceil_height
                screen.blit(ceil_sprite, (left, top))

    def build(self):
        for size in self.ships_sizes:
            self.place(size)
        self._initialized = True

    def check_up(self, size, x, y):
        flag = True
        for i in range(size):
            if (0 <= (x - i) < 10) and self.field_view[x - i][y] == 0:
                continue
            else:
                flag = False
        if flag:
            Ship(self, size, x, y, 1)
        else:
            self.place(size)

    def check_down(self, size, x, y):
        flag = True
        for i in range(size):
            if (0 <= (x + i) < 10) and self.field_view[x + i][y] == 0:
                continue
            else:
                flag = False
        if flag:
            Ship(self, size, x, y, 2)
        else:
            self.place(size)

    def check_left(self, size, x, y):
        flag = True
        for i in range(size):
            if (0 <= (y - i) < 10) and self.field_view[x][y - i] == 0:
                continue
            else:
                flag = False
        if flag:
            Ship(self, size, x, y, 3)
        else:
            self.place(size)

    def check_right(self, size, x, y):
        flag = True
        for i in range(size):
            if (0 <= (y + i) < 10) and self.field_view[x][y + i] == 0:
                continue
            else:
                flag = False
        if flag:
            Ship(self, size, x, y, 4)
        else:
            self.place(size)

    def place(self, size):
        x, y = self.free_spots[random.randint(0, len(self.free_spots) - 1)]
        d = random.randint(1, 4)
        if d == 1:
            self.check_up(size, x, y)
        if d == 2:
            self.check_down(size, x, y)
        if d == 3:
            self.check_left(size, x, y)
        if d == 4:
            self.check_right(size, x, y)
