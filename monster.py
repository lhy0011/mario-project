from pico2d import *
import random
import game_framework
import main_state
from mario import Mario

TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 0.5 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

MAX_X = 800
MAX_Y = 600

basicY = 83

EMAXHEIGHT = 267
EMAXWIDTH = 1683
ESIZE = 32

class Mgoomba: # 32x32
    image = None
    def __init__(self, x):
        Mgoomba.image = load_image('resource/enemies.png')
        self.frame = 0
        self.x = x
        self.y = basicY
        self.isTWL = False
        self.isTWR = True
        self. frame = 0
        self.fixX = 0

    def get_bb(self):
        return self.x - 15 - self.fixX, self.y - 20, self.x + 15 - self.fixX, self.y + 20

    def do(self):
        # self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        pass

    def update(self):

        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2
        if self.x < 0:
            self.isTWL = True
            self.isTWR = False
        if self.x > 300:
            self.isTWR = True
            self.isTWL = False
        if self.isTWL == False:
            self.x -= 0.5
        elif self.isTWR == False:
            self.x += 0.5

    def draw(self):
        global EMAXHEIGHT
        global EMAXWIDTH
        global ESIZE
        Mgoomba.image.clip_draw(int(self.frame) * 33, EMAXHEIGHT - ESIZE*2, 33, 32, self.x - self.fixX, self.y)
        draw_rectangle(*self.get_bb())

    def fix(self, xx):
        self.fixX = xx

class M:
    image = None
    def __init__(self):
        M.image = load_image('resource/enemies.png')
        self.frame = 0
        self.x = 700
        self.y = basicY
        self.fixX = 0

    def get_bb(self):
        return self.x - 15 - self.fixX, self.y - 20, self.x + 15 - self.fixX, self.y + 20

    def do(self):
        # self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        pass

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2
        mx = Mario.get_MX(main_state.player)

        # print(mx)


        if self.x > mx:
            if self.x - mx < 300:
                self.x -= 0.5
        elif self.x < mx:
            if mx - self.x < 300:
                self.x += 0.5

    def draw(self):
        global EMAXHEIGHT
        global EMAXWIDTH
        global ESIZE
        M.image.clip_draw(int(self.frame) * 33 + (33 * 3), EMAXHEIGHT - ESIZE*2, 33, 32, self.x - self.fixX, self.y)
        draw_rectangle(*self.get_bb())

    def fix(self, xx):
        self.fixX = xx

    def remove(self):
        self.x = -500
        self.y = -500