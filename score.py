from pico2d import *
import game_framework

TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 0.5 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Score:
    def __init__(self):
        self.font = load_font('ENCR10B.TTF', 32)
        self.image = load_image('resource/coin.png')
        self.sco = 0
        self.coin = 0
        self.frame = 0


    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4

    def draw(self):
        #점수표기
        self.font.draw(450, 560, 'SCORE', (255,255,255))
        self.font.draw(450, 530, '%d' % self.sco, (255,255,255))

        #코인개수표기
        self.image.clip_draw(int(self.frame) * 16, 0, 16, 16, 50,560, 34, 34)
        self.font.draw(80, 560, 'X', (255,255,255))
        self.font.draw(110, 560, '%d' % self.coin, (255,255,255))


    def stop(self):
        pass

    def fix(self, xx):
        pass