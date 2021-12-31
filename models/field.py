import os
import random
from typing import Union

import pygame

from config.config import Config
from effects import graphics
from effects import sound
from .ship import Ship


class Field:
    def __init__(self) -> None:
        self.sound = sound.Sound()

        self.size = self.width, self.height = Config.FIELD_WIDTH, Config.FIELD_HEIGHT
        self.cell_size = self.cell_width, self.cell_height = Config.CELL_WIDTH, Config.CELL_HEIGHT
        self.pix_size = self.pix_width, self.pix_height = Config.FIELD_PIX_WIDTH, Config.FIELD_PIX_HEIGHT

        self.border_weight = Config.CELL_BORDER_WEIGHT
        self.border_color = Config.CELL_BORDER_COLOR

        self._initialized = False

        self.clickable = False
        self.enemy = False
        self.types_to_make_invisible = Config.TYPES_TO_MAKE_INVISIBLE

        self.field_view = [[0 for j in range(self.height)] for i in range(self.width)]
        self.field_ships = [[Ship for j in range(self.height)] for i in range(self.width)]
        self.free_spots = []
        self.busy_cells = []
        self.ships_left = 10
        self.ship_cells_left = Config.WIN_SCORE
        for i in range(10):
            for j in range(10):
                self.free_spots.append((i, j))

        self.ships_sizes = Config.SHIPS_SIZES

        self.cell_sprites = []
        for filename in Config.CELL_SPRITES_FILENAMES:
            file_path = os.path.join('.', 'static', 'img', filename)
            sprite = pygame.image.load(file_path)
            sprite = pygame.transform.scale(sprite, self.cell_size)
            self.cell_sprites.append(sprite)

        self.build()

    @staticmethod
    def get_field_cords_by_screen_cords(surface_cords: tuple[int, int]) -> tuple[int, int]:
        screen_x, screen_y = surface_cords

        field_x = screen_x // (Config.CELL_WIDTH + Config.CELL_BORDER_WEIGHT)
        if field_x >= Config.FIELD_WIDTH:
            field_x = Config.FIELD_WIDTH - 1

        field_y = screen_y // (Config.CELL_HEIGHT + Config.CELL_BORDER_WEIGHT)
        if field_y >= Config.FIELD_HEIGHT:
            field_y = Config.FIELD_HEIGHT - 1

        return field_x, field_y

    def is_ship(self, field_cords: tuple[int, int]) -> bool:
        assert self._initialized
        x, y = field_cords
        return isinstance(self.field_ships[x][y], Ship)

    def click(self, cords: tuple[int, int]) -> Union[None, bool]:
        if not self.clickable:
            return

        field_cords = self.get_field_cords_by_screen_cords(cords)
        return self.shoot(field_cords)

    def shoot(self, field_cords: tuple[int, int]) -> bool:
        x, y = field_cords
        if field_cords not in self.busy_cells:
            graphics.FallingBomb(x, y, self)
            self.sound.boom()
            return self.is_ship(field_cords)
        return True

    def render(self, screen: pygame.Surface) -> None:
        assert self._initialized

        # draw grid from borders
        for col in range(self.width + 1):
            col_x = (self.border_weight + self.cell_width) * col
            start_pos = (col_x, 0)
            end_pos = (col_x, self.pix_height)
            pygame.draw.line(screen, self.border_color, start_pos, end_pos, width=self.border_weight)
        # draw last border
        x_last_start_pos = (self.pix_width - self.border_weight, 0)
        x_last_end_pos = (self.pix_width - self.border_weight, self.pix_height)
        pygame.draw.line(screen, self.border_color, x_last_start_pos, x_last_end_pos, width=self.border_weight)

        for row in range(self.height + 1):
            row_y = (self.border_weight + self.cell_height) * row
            start_pos = (0, row_y)
            end_pos = (self.pix_width, row_y)
            pygame.draw.line(screen, self.border_color, start_pos, end_pos, width=self.border_weight)

        y_last_start_pos = (0, self.pix_height - self.border_weight)
        y_last_end_pos = (self.pix_width, self.pix_height - self.border_weight)
        pygame.draw.line(screen, self.border_color, y_last_start_pos, y_last_end_pos, width=self.border_weight)

        for x in range(self.width):
            for y in range(self.height):
                cell_type = self.field_view[x][y]
                if self.enemy and cell_type in self.types_to_make_invisible:
                    cell_type = 0

                cell_sprite = self.cell_sprites[cell_type]
                left = (x + 1) * self.border_weight + x * self.cell_width
                top = (y + 1) * self.border_weight + y * self.cell_height
                screen.blit(cell_sprite, (left, top))
        for bomb, f in graphics.is_falling:
            if f == self:
                bomb.fall()
                screen.blit(bomb.sprite, (bomb.x, bomb.y))

    def build(self) -> None:
        for size in self.ships_sizes:
            self.place(size)
        self._initialized = True

    def activate_enemy(self) -> None:
        self.enemy = True

    def deactivate_enemy(self) -> None:
        self.enemy = False

    def is_enemy(self) -> bool:
        return self.enemy

    def activate_clickable(self) -> None:
        self.clickable = True

    def deactivate_clickable(self) -> None:
        self.clickable = False

    def is_clickable(self) -> bool:
        return self.clickable

    def check_up(self, ship_size: int, x: int, y: int) -> None:
        flag = True
        for i in range(ship_size):
            if (0 <= (x - i) < 10) and self.field_view[x - i][y] == 0:
                continue
            else:
                flag = False
        if flag:
            Ship(self, ship_size, x, y, 1)
        else:
            self.place(ship_size)

    def check_down(self, ship_size: int, x: int, y: int) -> None:
        flag = True
        for i in range(ship_size):
            if (0 <= (x + i) < 10) and self.field_view[x + i][y] == 0:
                continue
            else:
                flag = False
        if flag:
            Ship(self, ship_size, x, y, 2)
        else:
            self.place(ship_size)

    def check_left(self, ship_size: int, x: int, y: int) -> None:
        flag = True
        for i in range(ship_size):
            if (0 <= (y - i) < 10) and self.field_view[x][y - i] == 0:
                continue
            else:
                flag = False
        if flag:
            Ship(self, ship_size, x, y, 3)
        else:
            self.place(ship_size)

    def check_right(self, ship_size: int, x: int, y: int) -> None:
        flag = True
        for i in range(ship_size):
            if (0 <= (y + i) < 10) and self.field_view[x][y + i] == 0:
                continue
            else:
                flag = False
        if flag:
            Ship(self, ship_size, x, y, 4)
        else:
            self.place(ship_size)

    def place(self, ship_size: int) -> None:
        x, y = self.free_spots[random.randint(0, len(self.free_spots) - 1)]
        d = random.randint(1, 4)
        if d == 1:
            self.check_up(ship_size, x, y)
        if d == 2:
            self.check_down(ship_size, x, y)
        if d == 3:
            self.check_left(ship_size, x, y)
        if d == 4:
            self.check_right(ship_size, x, y)
