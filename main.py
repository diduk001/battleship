import pygame

from config import Config
from field import Field
from ui import UI


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.screen_size = self.screen_width, self.screen_height = Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT
        self.field_size = self.field_width, self.field_height = Config.FIELD_PIX_WIDTH, Config.FIELD_PIX_HEIGHT

        self.ui = UI()
        self.field = Field()
        self.field2 = Field()
        self._field_surface = pygame.Surface(self.field_size)
        self._field2_surface = pygame.Surface(self.field_size)

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.screen_size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption(Config.WINDOW_CAPTION)
        self._running = True

        self.ui.add((0, 0), self.field_size, self.field, self._field_surface)
        self.ui.add((602, 0), self.field_size, self.field2, self._field2_surface)
        self.field2.make_invisible()

    def on_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            self.ui.click(mouse_pos)
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        self.ui.render(self._display_surf)
        pygame.display.update()

    @staticmethod
    def on_cleanup():
        pygame.quit()

    def on_execute(self):
        if self.on_init() is False:
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
