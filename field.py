import pygame

from config import Config


class Field:
    def __init__(self) -> None:
        self.size = self.width, self.height = Config.FIELD_WIDTH, Config.FIELD_HEIGHT
        self.ceil_size = self.ceil_width, self.ceil_height = Config.CEIL_WIDTH, Config.CEIL_HEIGHT
        self.screen_size = self.screen_width, self.screen_height = Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT

        self.border_weight = Config.BORDER_WEIGHT
        self.border_color = Config.BORDER_COLOR

        self.ceil_colors = Config.CEIL_COLOR_BY_TYPE

        self._initialized = False
        self.field_view = [[0 for j in range(self.width)] for i in range(self.height)]
        self.field_ships = [[0 for j in range(self.width)] for i in range(self.height)]

    def render(self, screen: pygame.Surface) -> None:
        # assert self._initialized

        screen.fill((255, 255, 255))
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
                ceil_type = self.field_view[y][x]
                ceil_color = self.ceil_colors[ceil_type]

                left = (x + 1) * self.border_weight + x * self.ceil_width
                top = (y + 1) * self.border_weight + y * self.ceil_height
                width = self.ceil_width
                height = self.ceil_height
                rect = pygame.Rect(left, top, width, height)

                pygame.draw.rect(screen, ceil_color, rect)

    def get_field_cords_by_screen_cords(self, screen_cords: tuple[int, int]) -> tuple[int, int]:
        screen_x, screen_y = screen_cords

        field_x = screen_x // (self.ceil_width + self.border_weight)
        if field_x >= self.width:
            field_x = self.width - 1

        field_y = screen_y // (self.ceil_height + self.border_weight)
        if field_y >= self.height:
            field_y = self.height - 1

        return field_x, field_y

    def shoot(self, field_cords: tuple[int, int]) -> None:
        # TODO: bebra
        x_field, y_field = field_cords
        print(field_cords)
        self.field_view[y_field][x_field] = 1
