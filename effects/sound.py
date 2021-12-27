from os import path
from pygame import mixer
from config.config import Config

class Sound:
    sound_boom = mixer.Sound(path.join(path.curdir, 'static', 'music', Config.SOUND_BOOM_FILENAME))
    mixer.music.load(path.join(path.curdir, 'static', 'music', Config.SOUNDTRACK_FILENAME))

    @staticmethod
    def play_music():
        mixer.music.play()
    
    @staticmethod
    def stop_music():
        mixer.music.stop()

    @staticmethod
    def pause_music(b):
        if b:
            mixer.music.pause()
        else:
            mixer.music.unpause()

    def boom(self):
        self.sound_boom.play()
    