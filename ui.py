import pygame

from config import Config


class UI:
    def __init__(self) -> None:
        # list of ((x, y), (width, height) obj, surface)
        # obj must have .render(surface: pygame.Surface) method
        # obj must have .click(cords: tuple[int]) method
        self.objs = list()
        self.size = self.width, self.height = Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT

    def add(self, cords: tuple[int, int], size: tuple[int, int], obj, surf: pygame.Surface) -> None:
        # check if obj has render method
        assert hasattr(obj, 'render') and callable(getattr(obj, 'render'))
        # check if obj has click method
        assert hasattr(obj, 'click') and callable(getattr(obj, 'click'))

        self.objs.append((cords, size, obj, surf))

    def render(self, screen: pygame.Surface) -> None:
        for cords, size, obj, surface in self.objs:
            obj.render(surface)
            screen.blit(surface, cords)

    def click(self, click_cords: tuple[int, int]) -> None:
        click_x, click_y = click_cords
        for obj_cords, obj_size, obj, obj_surface in self.objs:
            obj_rect = pygame.Rect(obj_cords, obj_size)
            obj_rect_x, obj_rect_y = obj_cords
            if obj_rect.collidepoint(click_cords):
                obj.click((click_x - obj_rect_x, click_y - obj_rect_y))
