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
        self.item = load_music('sound/powerup.ogg')
        self.itemD = load_music('sound/powerup_appears.ogg')
        self.kick = load_music('sound/kick.ogg')
        self.coin = load_music('sound/coin.ogg')
        self.fireball = load_music('sound/fireball.ogg')

    def effectPlay(self, t=0):
        if t == 1:
            self.jump.play()
        elif t == 2:
            self.death.play()
        elif t == 3:
            self.item.play()
        elif t == 4:
            self.itemD.play()
        elif t == 5:
            self.kick.play()
        elif t == 6:
            self.coin.play()
        elif t == 7:
            self.fireball.play()