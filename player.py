import pygame

from config import Config
from field import Field
from ui import UI, Text


class Player(UI):
    def __init__(self, name='Unnamed'):
        self.name = name
        self.size = self.width, self.height = Config.PLAYER_UI_WIDTH, Config.PLAYER_UI_HEIGHT

        super().__init__(self.size)

        self.field = Field()
        super().add((0, 60), self.field.pix_size, self.field)

        self.font_name = Config.PLAYER_UI_FONT_NAME
        self.font_size = Config.PLAYER_UI_FONT_SIZE
        self.text = Text(self.name, pygame.font.SysFont(self.font_name, self.font_size), color=(255, 255, 255))
        super().add((0, 10), self.text.size, self.text)

    def render(self, screen: pygame.Surface) -> None:
        super().render(screen)

        # draw bounding box
        bounding_rect = pygame.Rect((0, 0), self.size)
        bounding_rect_color = Config.PLAYER_BORDER_COLOR
        pygame.draw.rect(screen, bounding_rect_color, bounding_rect, width=1)
