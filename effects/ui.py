from typing import Any, Iterable

import pygame


class UI:
    def __init__(self, size) -> None:
        # dict of d[name] = ((x, y), (width, height) obj)
        # obj must have .render(surface: pygame.Surface) method
        # obj must have .click(cords: tuple[int]) method
        self.objs = dict()
        self.size = self.width, self.height = size

    def add(self, name: str, cords: tuple[int, int], size: tuple[int, int], obj) -> None:
        # check if obj has render method
        assert hasattr(obj, 'render') and callable(getattr(obj, 'render'))
        # check if obj has click method
        assert hasattr(obj, 'click') and callable(getattr(obj, 'click'))

        self.objs[name] = (cords, size, obj)

    def render(self, screen: pygame.Surface) -> None:
        for cords, size, obj, in self.objs.values():
            surface = pygame.Surface(size)
            obj.render(surface)
            screen.blit(surface, cords)

    def click(self, click_cords: tuple[int, int]) -> Iterable[tuple[str, Any]]:
        click_x, click_y = click_cords
        for name, (obj_cords, obj_size, obj) in self.objs.items():
            obj_rect = pygame.Rect(obj_cords, obj_size)
            obj_rect_x, obj_rect_y = obj_cords
            if obj_rect.collidepoint(click_cords):
                yield name, obj.click((click_x - obj_rect_x, click_y - obj_rect_y))


# UI-compatible text class
class Text:
    def __init__(self, text: str, font: pygame.font.Font, color=(0, 0, 0)):
        self.text = text
        self.font = font
        self.color = color

        self.text_surface = self.font.render(self.text, True, self.color)
        self.size = self.width, self.height = self.text_surface.get_width(), self.text_surface.get_height()

    def click(self, click_cods: tuple[int, int]) -> None:
        pass

    def render(self, screen: pygame.Surface) -> None:
        screen.blit(self.text_surface, (0, 0))
