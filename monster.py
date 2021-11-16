from pico2d import *
import random
import mario

MAX_X = 800
MAX_Y = 600

basicY = 83

EMAXHEIGHT = 267
EMAXWIDTH = 1683
ESIZE = 32
frameE = 0

class Mgoomba: # 32x32
    def __init__(self):
        self.Goomba = load_image('resource/enemies.png')
        self.frame = 0
        self.x = random.randint (100, 300)
        self.y = basicY
        self.isTWL = False
        self.isTWR = True

    def update(self):
        global frameE
        if frameE % 16 == 0:
            self.frame = (self.frame + 1) % 2
        frameE += 1
        if self.x < 0:
            self.isTWL = True
            self.isTWR = False
        if self.x > 800:
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
        self.Goomba.clip_draw(self.frame * 32, EMAXHEIGHT - ESIZE*2, 32, 32, self.x, self.y)
        pass

class M:
    def __init__(self):
        self.mAI = load_image('resource/enemies.png')
        self.frame = 0
        self.x = random.randint(100,300)
        self.y = basicY

    def update(self):
        global frameE
        if frameE % 16 == 0:
            self.frame = (self.frame + 1) % 2
        frameE += 1
        mx = mario.Mario.getMX(self)

        print(mx)

        # while (self.x == mx):
        #     if self.x > mx:
        #         if self.x - mx < 40:
        #             self.x += 3
        #     elif self.x < mx:
        #         if mx - self.x < 40:
        #             self.x -= 3

    def draw(self):
        global EMAXHEIGHT
        global EMAXWIDTH
        global ESIZE
        self.mAI.clip_draw(self.frame * 32 + (32 * 3), EMAXHEIGHT - ESIZE*2, 32, 32, self.x, self.y)
        pass
