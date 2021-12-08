from pico2d import *
import random
import mario
import map1
import game_framework

TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 0.5 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

MAXHEIGHT = 933
MAXWIDTH = 1100
SIZES = 34
SIZEB = 68
MAX_X = 800
MAX_Y = 600

basicY = 83

#size * 1 = 벽돌, size * 9~10 파이프

class Ground: # 34x34
    image = None
    def __init__(self, x = 0):
        Ground.image = load_image('resource/tile_set.png')
        self.x = x
        self.y = 51
        self.fixX = 0

    def draw(self):
        global SIZES
        global SIZEB
        global MAXHEIGHT
        global MAXWIDTH
        global MAX_X
        global MAX_Y


        groundX = 51
        groundY = 51
        #
        # for i in range(len(map1.Map1.ground)):
        #     self.x = map1.Map1.ground[i]
        #     # Ground.image.clip_draw(0, MAXHEIGHT - SIZES, SIZES, SIZES, map1.Map1.ground[i] - self.fixX, groundY)
        #     # Ground.image.clip_draw(0, MAXHEIGHT - SIZES, SIZES, SIZES, map1.Map1.ground[i] - self.fixX, groundY-SIZES)
        #     # print(map1.Map1.ground[i])
        #
        #     Ground.image.clip_draw(0, MAXHEIGHT - SIZES, SIZES, SIZES, self.x - self.fixX, groundY)
        #     Ground.image.clip_draw(0, MAXHEIGHT - SIZES, SIZES, SIZES, self.x - self.fixX, groundY - SIZES)
        #     # draw_rectangle(*self.get_bb())

        pass

    def update(self):
        pass

    def fix(self, xx):
        self.fixX = xx

    def get_bb(self):
        return self.x - 17 - self.fixX, self.y - 17, self.x + 17 - self.fixX, self.y + 17



class Grounds: # 34x34
    image = None
    def __init__(self, x):
        Grounds.image = load_image('resource/tile_set.png')
        self.x = x
        self.y = 51
        self.fixX = 0

    def draw(self):
        global SIZES
        global SIZEB
        global MAXHEIGHT
        global MAXWIDTH
        global MAX_X
        global MAX_Y


        groundX = 51
        groundY = 51
        # for i in range(len(map1.Map1.ground)):
        #     draw_rectangle(*self.get_bb())

        Grounds.image.clip_draw(0, MAXHEIGHT - SIZES, SIZES, SIZES, self.x - self.fixX, groundY)
        Grounds.image.clip_draw(0, MAXHEIGHT - SIZES, SIZES, SIZES, self.x - self.fixX, groundY - SIZES)

        pass

    def update(self):
        pass

    def fix(self, xx):
        self.fixX = xx

    def get_bb(self):
        return self.x - 17 - self.fixX, self.y - 17, self.x + 17 - self.fixX, self.y + 17

class Block:
    image = None
    def __init__(self, x):
        Block.image = load_image('resource/tile_set.png')
        self.x = x
        self.y = 204
        self.fixX = 0

    def draw(self):
        Block.image.clip_draw(SIZES, MAXHEIGHT - SIZES, SIZES, SIZES, self.x - self.fixX, self.y, 34, 34)
        draw_rectangle(*self.get_bb())
        pass

    def update(self):
        pass

    def fix(self, xx):
        self.fixX = xx

    def get_bb(self):
        return self.x - 17 - self.fixX, self.y - 17, self.x + 17 - self.fixX, self.y + 17


class RandBoxC:
    image = None
    def __init__(self, x):
        Block.image = load_image('resource/tile_set.png')
        self.x = x
        self.y = 204
        self.fixX = 0
        self.frame = 0
        self.isBreak = False

    def draw(self):
        if self.isBreak == False:
            Block.image.clip_draw(800 + SIZES * int(self.frame)-1, MAXHEIGHT - SIZES, SIZES, SIZES, self.x - self.fixX, self.y, 34, 34)
            draw_rectangle(*self.get_bb())
        else:
            Block.image.clip_draw(900, MAXHEIGHT - SIZES, SIZES, SIZES, self.x - self.fixX, self.y, 34, 34)
            draw_rectangle(*self.get_bb())
        pass

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        pass

    def fix(self, xx):
        self.fixX = xx

    def get_bb(self):
        return self.x - 17 - self.fixX, self.y - 17, self.x + 17 - self.fixX, self.y + 17

class RandBoxI:
    image = None
    def __init__(self, x):
        Block.image = load_image('resource/tile_set.png')
        self.x = x
        self.y = 204
        self.fixX = 0
        self.frame = 0
        self.isBreak = False

    def draw(self):
        if self.isBreak == False:
            Block.image.clip_draw(800 + SIZES * int(self.frame)-1, MAXHEIGHT - SIZES, SIZES, SIZES, self.x - self.fixX, self.y, 34, 34)
            draw_rectangle(*self.get_bb())
        else:
            Block.image.clip_draw(900, MAXHEIGHT - SIZES, SIZES, SIZES, self.x - self.fixX, self.y, 34, 34)
            draw_rectangle(*self.get_bb())
        pass

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        pass

    def fix(self, xx):
        self.fixX = xx

    def get_bb(self):
        return self.x - 17 - self.fixX, self.y - 17, self.x + 17 - self.fixX, self.y + 17

###### 아이템  16x16

class Coin:
    image = None
    def __init__(self, x):
        Coin.image = load_image('resource/coin.png')
        self.frame = 0
        self.x, self.y = x, 238
        self.fixX = 0

    def draw(self):
        for i in range(len(map1.Map1.coin)):
            Coin.image.clip_draw(int(self.frame) * 16, 0, 16, 16, self.x - self.fixX, self.y, 34, 34)
            # Coin.image.clip_draw(int(self.frame) * 16, 0, 16, 16, map1.Map1.coin[i] - self.fixX, self.y, 34, 34)
            draw_rectangle(*self.get_bb())
        pass

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        pass

    def fix(self, xx):
        self.fixX = xx

    def get_bb(self):
        return self.x - 15 - self.fixX, self.y - 17, self.x + 15 - self.fixX, self.y + 17


class Item1:
    image = None

    def __init__(self):
        Item1.image = load_image('resource/item1.png')
        self.frame = 0
        self.x, self.y = 0, 0
        self.fixX = 0

    def draw(self):
        Item1.image.clip_draw(int(self.frame) * 16, 0, 16, 16, self.x - self.fixX, self.y)
        pass

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        pass

    def fix(self, xx):
        self.fixX = xx

    def get_bb(self):
        return self.x - 17 - self.fixX, self.y - 17, self.x + 17 - self.fixX, self.y + 17


class Item2:
    image = None

    def __init__(self):
        Item2.image = load_image('resource/item2.png')
        self.frame = 0
        self.x, self.y = 700, 83
        self.fixX = 0

    def draw(self):
        Item2.image.clip_draw(int(self.frame) * 16, 0, 16, 16, self.x - self.fixX, self.y, 34, 34)
        draw_rectangle(*self.get_bb())
        pass

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        pass

    def fix(self, xx):
        self.fixX = xx

    def get_bb(self):
        return self.x - 17 - self.fixX, self.y - 17, self.x + 17 - self.fixX, self.y + 17

    def remove(self):
        self.x = -500
        self.y = -500



##### 배경 (오브젝트X)

class BG: # 배경 사진
    def __init__(self):
        self.bg = load_image('resource/background.png')
    def draw(self):
        self.bg.draw(500, 500)
    def update(self):
        pass
    def fix(self, xx):
        self.fixX = xx

class Cloud: # 그 외 배경
    image = None
    def __init__(self):
        Cloud.image = load_image('resource/tile_set.png')
        self.x = 0
        self.y = 0
        self.fixX = 0
    def draw(self):
        for i in range(6):
            Cloud.image.clip_draw(0, 0, (SIZES-1) * 3, (SIZES-1) * 2, 1000 * i - self.fixX, 500)
            Cloud.image.clip_draw(0, 0, (SIZES-1) * 3, (SIZES-1) * 2, 1000 * i - self.fixX +500, 400)

        pass
    def update(self):
        pass
    def fix(self, xx):
        self.fixX = xx

class Tree:
    def __init__(self):
        self.tree = load_image('resource/tile_set.png')
        self.x = 0
        self.y = 0
        self.fixX = 0
    def draw(self):
        pass
    def update(self):
        pass
    def fix(self, xx):
        self.fixX = xx
