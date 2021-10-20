from pico2d import *
import mario

class BGM:
    def __init__(self):
        self.mainTheme = load_music('bgm/main_theme.ogg')
        self.mainTheme.play()

class EFFECT:
    def __init__(self):
        self.jump = load_music('sound/small_jump.ogg')
        self.death = load_wav('sound/death.wav')
