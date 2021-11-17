from pico2d import *
import random
import mario

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
    def draw(self):
        self.bg.draw(500, 500)
    def update(self):
        pass

class BGG: # 그 외 배경
    def __init__(self):
        self.cloud = load_image('resource/tile_set.png')
    def drawBGG(self):
        pass

class Ground: # 34x34
    def __init__(self):
        self.tile = load_image('resource/tile_set.png')
    pass
    def draw(self):
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

    def update(self):
        pass


