from pico2d import *
import keyboard as k

MOVING = True
DIRECL = False
MAXSPEED = 5
MAXHEIGHT = 150 # 점프높이
frameS = 0
isJump = False
isBreakR = False
isBreakL = False
isDescend = False

basicY = 83

def cmove():
    global MOVING
    global DIRECL
    global isJump
    global isBreakR
    global isBreakL
    global dir  # -1 : left // 1 : right
    dir = 0

    if k.is_pressed('right'):
        DIRECL = False
        dir += 1
        #print('오른쪽')
        if k.is_pressed('left'):
            isBreakL = True
            DIRECL = True
            dir = -1
        elif k.is_pressed('a'):
            isJump = True

    elif k.is_pressed('left'):
        DIRECL = True
        dir -= 1
        #print('왼쪽')
        if k.is_pressed('right'):
            isBreakR = True
            DIRECL = False
            dir = 1
        elif k.is_pressed('a'):
            isJump = True

    elif k.is_pressed("a"):
        isJump = True


    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            MOVING = False
        elif e.type == SDL_KEYDOWN and e.type == SDLK_a:
            isJump = True



class Mario: #
    def __init__(self):
        self.marioRR = load_image('resource/marioRunR.png')
        self.marioRL = load_image('resource/marioRunL.png')
        self.marioR = load_image('resource/marioStandR.png')
        self.marioL = load_image('resource/marioStandL.png')
        self.marioJR = load_image('resource/marioJumpR.png')
        self.marioJL = load_image('resource/marioJumpL.png')
        self.marioBR = load_image('resource/marioBreakR.png')
        self.marioBL = load_image('resource/marioBreakL.png')
        self.frame = 0
        self.speedX = 0.0
        self.speedY = 5
        self.x = 400
        self.y = basicY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def update(self):
        global MAXSPEED
        global frameS
        global isBreak
        global isJump
        global isDescend
        global isBreakR
        global isBreakL

        if isJump == True:
            if self.y < (basicY + MAXHEIGHT):
                self.y += self.speedY
            elif self.y == (basicY + MAXHEIGHT):
                isJump = False
                isDescend = True
        elif isJump == False:
            if self.y > basicY:
                self.y -= self.speedY
            elif self.y == basicY:
                isDescend = False

        if isBreakR == True:
            isBreakR = False

        if isBreakL == True:
            isBreakL = False

        # 속도 점점빠르게
        if self.speedX < MAXSPEED:
            self.speedX += 0.04
        self.x += (dir * self.speedX)

        # 미끄러지는 효과 ... 일단시도
        # if dir == 0 and self.speedX > 1:
        #     if DIRECL == False:
        #         self.speedX -= 0.6
        #         self.x += 0.6
        #     elif DIRECL == True:
        #         self.speedX -= 0.6
        #         self.x -= 0.6

        if dir == 0 and self.speedX > 1:
            self.speedX = 0

        # 프레임 속도 조절
        if frameS % 8 == 0:
            self.frame = (self.frame + 1) % 3
        frameS += 1


    def draw(self):
        global dir
        global isJump

        if isJump == True and DIRECL == False: #jump
            self.marioJR.draw(self.x, self.y)
        elif isJump == True and DIRECL == True:
            self.marioJL.draw(self.x, self.y)
        elif isDescend == True and DIRECL == False:
            self.marioJR.draw(self.x, self.y)
        elif isDescend == True and DIRECL == True:
            self.marioJR.draw(self.x, self.y)

        elif isBreakR == True and DIRECL == False:
            self.marioBR.draw(self.x, self.y)
        elif isBreakL == True and DIRECL == True:
            self.marioBL.draw(self.x, self.y)


        elif dir == 0 and DIRECL == False: #stand
            self.marioR.draw(self.x, self.y)
        elif dir == 0 and DIRECL == True:
            self.marioL.draw(self.x, self.y)
        elif dir == 1 and isJump == False : #run
            self.marioRR.clip_draw(self.frame * 36, 0, 36, 34, self.x, self.y)
        elif dir == -1 and isJump == False :
            self.marioRL.clip_draw(self.frame * 36, 0, 36, 34, self.x, self.y)




