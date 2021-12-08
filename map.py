from pico2d import *
import random

import game_world
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

class Block2:
    image = None
    def __init__(self, x, y = 85):
        Block2.image = load_image('resource/tile_set.png')
        self.x = x
        self.y = y
        self.fixX = 0

    def draw(self):
        Block2.image.clip_draw(0, MAXHEIGHT - SIZES * 2, SIZES, SIZES, self.x - self.fixX, self.y, 34, 34)
        draw_rectangle(*self.get_bb())
        pass

    def update(self):
        pass

    def fix(self, xx):
        self.fixX = xx

    def get_bb(self):
        return self.x - 17 - self.fixX, self.y - 17, self.x + 17 - self.fixX, self.y + 17

class Pipe1:
    image = None
    def __init__(self, x):
        Pipe1.image = load_image('resource/pipe1.png')
        self.x = x
        self.y = 102
        self.fixX = 0

    def draw(self):
        Pipe1.image.draw(self.x - self.fixX, self.y, 68, 68)
        draw_rectangle(*self.get_bb())
        pass

    def update(self):
        pass

    def fix(self, xx):
        self.fixX = xx

    def get_bb(self):
        return self.x - 34 - self.fixX, self.y - 34, self.x + 34 - self.fixX, self.y + 34

class Pipe2:
    image = None
    def __init__(self, x):
        Pipe2.image = load_image('resource/pipe2.png')
        self.x = x
        self.y = 136
        self.fixX = 0

    def draw(self):
        Pipe1.image.draw(self.x - self.fixX, self.y, 68, 136)
        draw_rectangle(*self.get_bb())
        pass

    def update(self):
        pass

    def fix(self, xx):
        self.fixX = xx

    def get_bb(self):
        return self.x - 34 - self.fixX, self.y - 68, self.x + 34 - self.fixX, self.y + 68


class RandBoxC:
    image = None
    imageC = None
    def __init__(self, x):
        RandBoxC.image = load_image('resource/tile_set.png')
        RandBoxC.imageC = load_image('resource/coin.png')
        self.x = x
        self.y = 204
        self.cy = 204
        self.fixX = 0
        self.frame = 0
        self.isBreak = False
        self.isSound = False
        self.count = 12
        self.S_b = load_music('sound/coin.ogg')

    def draw(self):
        if self.isBreak == False:
            RandBoxC.image.clip_draw(800 + SIZES * int(self.frame)-1, MAXHEIGHT - SIZES, SIZES, SIZES, self.x - self.fixX, self.y, 34, 34)
            draw_rectangle(*self.get_bb())
        else:
            RandBoxC.image.clip_draw(900, MAXHEIGHT - SIZES, SIZES, SIZES, self.x - self.fixX, self.y, 34, 34)
            draw_rectangle(*self.get_bb())
            if (self.count <= 12 and self.count > 8) or (self.count <= 4 and self.count > 0):
                RandBoxC.imageC.clip_draw(16, 0, 16, 16, self.x - self.fixX, self.y + 34, 34, 34)
                self.count -= 1
            elif self.count <= 8 and self.count > 4:
                RandBoxC.imageC.clip_draw(16, 0, 16, 16, self.x - self.fixX, self.y + 34 + 5, 34, 34)
                self.count -= 1

        pass

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        if self.count == 11:
            self.S_b.play()
        pass

    def fix(self, xx):
        self.fixX = xx

    def get_bb(self):
        return self.x - 20 - self.fixX, self.y - 17, self.x + 20 - self.fixX, self.y + 17

class RandBoxI:
    image = None
    def __init__(self, x):
        Block.image = load_image('resource/tile_set.png')
        self.x = x
        self.y = 204
        self.fixX = 0
        self.frame = 0
        self.isBreak = False
        self.isItem = False
        self.count = 1
        self.S_bs = load_music('sound/brick_smash.ogg')

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
        if self.isBreak == True:
            if self.count == 1:
                self.S_bs.play()
            self.count -= 1
            if self.isItem == False:
                self.isItem = True
                i2 = Item2(self.x, self.y + 34)
                game_world.add_object(i2, 4)

        pass

    def fix(self, xx):
        self.fixX = xx

    def get_bb(self):
        return self.x - 19 - self.fixX, self.y - 17, self.x + 19 - self.fixX, self.y + 17

###### 아이템  16x16

class Coin:
    image = None
    def __init__(self, x):
        Coin.image = load_image('resource/coin.png')
        self.frame = 0
        self.x, self.y = x, 238
        self.fixX = 0
        self.S_c = load_music('sound/coin.ogg') #아직 재생X


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

    def remove(self):
        self.S_c.play()
        self.x, self.y = -500, -500


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

    def __init__(self, x, y):
        Item2.image = load_image('resource/item2.png')
        self.frame = 0
        self.x, self.y = x, y
        self.fixX = 0
        self.S_i = load_music('sound/powerup.ogg')

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
        self.S_i.play()
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
