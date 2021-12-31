import pygame

from config.config import Config
from effects.sound import Sound
from effects.ui import UI
from models.player import Player


class App:
    def __init__(self):
        self._running = True
        self.screen_size = self.screen_width, self.screen_height = Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT
        self.field_size = self.field_width, self.field_height = Config.FIELD_PIX_WIDTH, Config.FIELD_PIX_HEIGHT

        self.sound = Sound()
        self.sound.play_music()

        self._display_surf = pygame.display.set_mode(self.screen_size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption(Config.WINDOW_CAPTION)
        self._running = True

        self.ui = UI(self.screen_size)

        self.passing_turn = False

        # creating players
        self.players_cnt = Config.PLAYERS_CNT
        self.cur_player_idx = 0
        self.players = [Player(name=f"Player {i + 1}") for i in range(self.players_cnt)]

        x = 0
        for i in range(self.players_cnt):
            y = 0
            self.ui.add(f"Player{i + 1}_UI", (x, y), self.players[i].size, self.players[i])

            x += self.players[i].width

    def on_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            if self.passing_turn:
                self.passing_turn = False
                return

            enemies_ui_names = [f"Player{i + 1}_UI" for i in range(self.players_cnt) if i != self.cur_player_idx]
            for name, gen in self.ui.click(mouse_pos):
                if name in enemies_ui_names:
                    # print(name)
                    to_ship_cur = list(gen)[0][1]
                    if to_ship_cur is True:
                        break
                else:
                    # Not clicked on field
                    break
            else:
                self.passing_turn = True
                self.cur_player_idx += 1
                self.cur_player_idx %= self.players_cnt

        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        for i in range(self.players_cnt):
            if not self.passing_turn and i == self.cur_player_idx:
                self.players[i].deactivate_enemy()
                self.players[i].deactivate_clickable()
            else:
                self.players[i].activate_enemy()
                self.players[i].activate_clickable()

        self.ui.render(self._display_surf)
        pygame.display.update()

    @staticmethod
    def on_cleanup():
        pygame.quit()

    def on_execute(self):
        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__":
    app = App()
    app.on_execute()
