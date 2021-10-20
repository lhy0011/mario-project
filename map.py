from pico2d import *
import random

MAXHEIGHT = 933
MAXWIDTH = 1100
SIZES = 34
SIZEB = 68
MAX_X = 800
MAX_Y = 600

basicY = 83

#size * 1 = 벽돌, size * 9~10 파이프

class BG: # 배경 사진
    def __init__(self):
        self.bg = load_image('resource/background.png')
    def drawBG(self):
        self.bg.draw(500, 500)

class BGG: # 그 외 배경
    def __init__(self):
        self.bgg = load_image('resource/tile_set.png')

class Ground: # 34x34
    def __init__(self):
        self.tile = load_image('resource/tile_set.png')
    pass
    def drawGround(self):
        global SIZES
        global SIZEB
        global MAXHEIGHT
        global MAXWIDTH
        global MAX_X
        global MAX_Y

        groundX = 51
        groundY = 51

        for i in range(30):
            self.tile.clip_draw(0, MAXHEIGHT - SIZES, SIZES, SIZES, SIZES * i, groundY)
            self.tile.clip_draw(0, MAXHEIGHT - SIZES, SIZES, SIZES, SIZES * i, groundY-SIZES)

        pass


EMAXHEIGHT = 267
EMAXWIDTH = 1683
ESIZE = 32
frameE = 0

class Monster: # 32x32
    def __init__(self):
        self.Goomba = load_image('resource/enemies.png')
        self.frame = 0
        self.x = random.randint (100, 300)
        self.y = basicY

    def update(self):
        global frameE
        if frameE % 16 == 0:
            self.frame = (self.frame + 1) % 2
        frameE += 1
        self.x -= 0.5

    def draw(self):
        global EMAXHEIGHT
        global EMAXWIDTH
        global ESIZE
        self.Goomba.clip_draw(self.frame * 32, EMAXHEIGHT - ESIZE*2, 32, 32, self.x, self.y)
        pass
