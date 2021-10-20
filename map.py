from pico2d import *

MAXHEIGHT = 933
MAXWIDTH = 1100
SIZES = 34
SIZEB = 68
MAX_X = 800
MAX_Y = 600

#size * 1 = 벽돌, size * 9~10 파이프

class BG:
    def __init__(self):
        self.bg = load_image('resource/background.png')
    def drawBG(self):
        self.bg.draw(500, 500)


class Ground:
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

class Monster:
    pass
