import pygame

from config import Config
from field import Field


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.screen_size = self.screen_width, self.screen_height = Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT

        self.field = Field()

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.screen_size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

    def on_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            field_cords = self.field.get_field_cords_by_screen_cords(mouse_pos)
            self.field.shoot(field_cords)
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        self.field.render(self._display_surf)
        pygame.display.update()

    @staticmethod
    def on_cleanup():
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
