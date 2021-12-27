from os import path
import pygame as pg
from pygame import mixer


class Sound:
    pg.init()
    sound1 = mixer.Sound(path.join(path.curdir, 'static/music/boom.mp3'))
    music = mixer.music.load(path.join(path.curdir, 'static/music/beethoven.ogg'))

    def play_music(self):
        mixer.music.play()
    
    def stop_music(self):
        mixer.music.stop()

    def pause_music(self, b):
        if b:
            mixer.music.pause()
        else:
            mixer.music.unpause()

    def boom(self):
        self.sound1.play()
    