import game_framework
from pico2d import *

import main_state
from fireball import fireBall
import sound

import game_world
import gameover_state

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 40.0  # Km / Hour
RUN_SPEED_PPS = (RUN_SPEED_KMPH * 1000.0 / 60.0 / 60.0 * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

JUMP_MAX_SPEED = 500
JUMP_MIN_SPEED = 100
JUMP_GRAVITY = 10

basicY = 83
MAXSPEED = 5
MAXHEIGHT = 250 # 점프높이
frameS = 0

EEE = None

RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, DASH_TIMER, A_DOWN, D_DOWN, CROUCH_DOWN, CROUCH_UP, DEAD, FIRE = range(11)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    #(SDL_KEYDOWN, SDLK_DOWN): CROUCH_DOWN, # 웅크리기
    #(SDL_KEYUP, SDLK_DOWN): CROUCH_UP,
    (SDL_KEYDOWN, SDLK_a): A_DOWN, # 점프
    (SDL_KEYDOWN, SDLK_d): D_DOWN # 공격버튼 //
}

# Boy States


class IdleState:

    def enter(mario, event):
        if event == RIGHT_DOWN:
            mario.velocity += RUN_SPEED_PPS
            mario.dir = 1
        elif event == LEFT_DOWN:
            mario.velocity -= RUN_SPEED_PPS
            mario.dir = -1
        elif event == RIGHT_UP:
            mario.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            mario.velocity += RUN_SPEED_PPS
        mario.timer = 100

    def exit(mario, event):
        if event == A_DOWN:
            mario.isJump = True
            mario.jumpSpeed = JUMP_MAX_SPEED
            mario.S_j.play()
            mario.descSpeed = 0

        if event == D_DOWN:
            if mario.ma2:
                mario.fireball()
        pass

    def do(mario):
        if mario.isJump == True:
            if mario.jumpSpeed > JUMP_MIN_SPEED:
                mario.y += mario.jumpSpeed * game_framework.frame_time
                mario.jumpSpeed -= JUMP_GRAVITY * game_framework.frame_time
            else:
                mario.y += mario.jumpSpeed * game_framework.frame_time
        if mario.y > (mario.curY + MAXHEIGHT):
            mario.isDescend = True
            mario.isJump = False
        if mario.isJump == False and mario.isDescend == True:
            if mario.jumpSpeed < JUMP_MAX_SPEED:
                mario.y -= mario.jumpSpeed * game_framework.frame_time
                mario.jumpSpeed += JUMP_GRAVITY * game_framework.frame_time
            else:
                mario.y -= mario.jumpSpeed * game_framework.frame_time
            if int(mario.y) <= basicY:
                mario.isDescend = False

        # if mario.y > basicY+2:
        #     mario.y -= mario.jumpSpeed * game_framework.frame_time
        pass

    def draw(mario):
        if mario.dir == 1:
            if mario.isJump or mario.isDescend:
                if mario.ma2:
                    mario.mario2J.draw(mario.x - mario.fixX, mario.y)
                else:
                    mario.marioJR.draw(mario.x - mario.fixX, mario.y)
            else:
                if mario.ma2:
                    mario.mario2.draw(mario.x - mario.fixX, mario.y)
                elif mario.isMM:
                    mario.marioD.draw(mario.x - mario.fixX, mario.y)
                else:
                    mario.marioR.draw(mario.x - mario.fixX, mario.y)
        else:
            if mario.isJump or mario.isDescend:
                if mario.ma2:
                    mario.mario2J.clip_composite_draw(0, 0, 36, 34, 0, 'h', mario.x - mario.fixX, mario.y)
                else:
                    mario.marioJL.draw(mario.x - mario.fixX, mario.y)
            else:
                if mario.ma2:
                    mario.mario2.clip_composite_draw(0, 0, 36, 34, 0, 'h', mario.x - mario.fixX, mario.y)
                elif mario.isMM:
                    mario.marioD.draw(mario.x - mario.fixX, mario.y)
                else:
                    mario.marioL.draw(mario.x - mario.fixX, mario.y)

class RunState:
    def enter(mario, event):
        global EEE
        if event == RIGHT_DOWN:
            EEE = RIGHT_DOWN
            mario.velocity += RUN_SPEED_PPS
            mario.dir = 1
        elif event == LEFT_DOWN:
            EEE = LEFT_DOWN
            mario.velocity -= RUN_SPEED_PPS
            mario.dir = -1
        elif event == RIGHT_UP:
            mario.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            mario.velocity += RUN_SPEED_PPS
        #mario.dir = clamp(-1, mario.velocity, 1)

    def exit(mario, event):
        if event == A_DOWN:
            mario.isJump = True
            mario.jumpSpeed = JUMP_MAX_SPEED
            mario.S_j.play()
        if event == D_DOWN:
            if mario.ma2:
                mario.fireball()
        pass

    def do(mario):
        global EEE
        mario.frame = (mario.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        mario.x += mario.velocity * game_framework.frame_time * mario.xstop
        # mario.x = clamp(25, mario.x, 500)
        if mario.isJump == True:
            if mario.jumpSpeed > JUMP_MIN_SPEED:
                mario.y += mario.jumpSpeed * game_framework.frame_time
                mario.jumpSpeed -= JUMP_GRAVITY * game_framework.frame_time
            else:
                mario.y += mario.jumpSpeed * game_framework.frame_time
        if mario.y > (mario.curY + MAXHEIGHT):
            mario.isDescend = True
            mario.isJump = False
        if mario.isJump == False and mario.isDescend == True:
            if mario.jumpSpeed < JUMP_MAX_SPEED:
                mario.y -= mario.jumpSpeed * game_framework.frame_time
                mario.jumpSpeed += JUMP_GRAVITY * game_framework.frame_time
            else:
                mario.y -= mario.jumpSpeed * game_framework.frame_time
            if int(mario.y) <= basicY:
                mario.isDescend = False

        for i in game_world.all_objects2(2):
            if mario.collide(i):
                if mario.y < i.y -15:
                    if mario.x >= i.x:
                        if EEE == LEFT_DOWN:
                            mario.isXstop = True
                        if EEE == RIGHT_DOWN:
                            mario.isXstop = False
                    elif mario.x <= i.x:
                        if EEE == RIGHT_DOWN:
                            mario.isXstop = True
                        if EEE == LEFT_DOWN:
                            mario.isXstop = False
                    else:
                        mario.isXstop = False

        pass

    def draw(mario):
        if mario.dir == 1:
            if mario.isJump or mario.isDescend:
                if mario.ma2:
                    mario.mario2J.draw(mario.x - mario.fixX, mario.y)
                else:
                    mario.marioJR.draw(mario.x - mario.fixX, mario.y)
            else:
                if mario.ma2:
                    mario.mario2R.clip_draw(int(mario.frame) * 36, 0, 36, 34, mario.x - mario.fixX, mario.y)
                elif mario.isMM:
                    mario.marioD.draw(mario.x - mario.fixX, mario.y)
                else:
                    mario.marioRR.clip_draw(int(mario.frame) * 36, 0, 36, 34, mario.x - mario.fixX, mario.y)
        else:
            if mario.isJump or mario.isDescend:
                if mario.ma2:
                    mario.mario2J.clip_composite_draw(0, 0, 36, 34, 0, 'h', mario.x - mario.fixX, mario.y)
                else:
                    mario.marioJL.draw(mario.x - mario.fixX, mario.y)
            else:
                if mario.ma2:
                    mario.mario2R.clip_composite_draw(int(mario.frame) * 36, 0, 36, 34, 0, 'h', mario.x - mario.fixX, mario.y, 36, 34)
                elif mario.isMM:
                    mario.marioD.draw(mario.x - mario.fixX, mario.y)
                else:
                    mario.marioRL.clip_draw(int(mario.frame) * 36, 0, 36, 34, mario.x - mario.fixX, mario.y)


class DeadState:
    def enter(mario, event):
        pass

    def exit(mario, event):
        pass

    def do(mario):
        pass

    def draw(mario):
        mario.marioD.draw(mario.x - mario.fixX, mario.y)
        mario.isdeadM = True






next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, A_DOWN: IdleState, D_DOWN: IdleState, DEAD: DeadState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, A_DOWN: RunState, D_DOWN: RunState, DEAD: DeadState},
    DeadState: {RIGHT_UP: DeadState, LEFT_UP: DeadState, RIGHT_DOWN: DeadState, LEFT_DOWN: DeadState, A_DOWN: DeadState, D_DOWN: DeadState}
}



class Mario: #
    def __init__(self):
        self.marioRR = load_image('resource/marioRunR.png')
        self.marioRL = load_image('resource/marioRunL.png')
        self.marioR = load_image('resource/marioStandR.png')
        self.marioL = load_image('resource/marioStandL.png')
        self.marioJR = load_image('resource/marioJumpR.png')
        self.marioJL = load_image('resource/marioJumpL.png')
        self.marioD = load_image('resource/marioDead.png')
        self.mario2 = load_image('resource/mario2_stand.png')
        self.mario2J = load_image('resource/mario2_jump.png')
        self.mario2R = load_image('resource/mario2_run.png')
        # self.marioC = load_image('resource/')
        self.velocity = 0
        self.frame = 0
        self.dir = 1
        self.speedX = 0.0
        self.speedY = 5
        self.x = 150
        self.y = 2500
        self.font = load_font('ENCR10B.TTF', 16)
        self.curY = 0

        self.descSpeed = 0

        self.colground = False

        self.isJump = False
        self.jumpSpeed= JUMP_MAX_SPEED
        self.isDescend = False
        self.isdeadM = False
        self.ma2 = False
        self.descendSpeed = JUMP_MIN_SPEED
        self.isMM = False
        self.htime = 0
        self.ctime = 0

        self.isXstop = False
        self.xstop = 1

        self.life = 1

        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        self.fixX = 0

        self.S_j = load_music('sound/small_jump.ogg')
        self.S_d = load_wav('sound/death.wav')
        self.S_f = load_music('sound/fireball.ogg')
        self.S_i = load_music('sound/powerup.ogg')
        self.S_i2 = load_music('sound/powerup_appears.ogg')

    def add_event(self, event):
        self.event_que.insert(0, event)

    def fireball(self):
        ball = fireBall(self.x - self.fixX, self.y, self.dir)
        game_world.add_object(ball, 1)
        self.S_f.play()

    def get_MX(self):
        return self.x

    def get_MY(self):
        return self.y

    def get_bb(self):
        return self.x - 15 - self.fixX, self.y - 20, self.x + 15 - self.fixX, self.y + 20

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

        # self.y -= self.descSpeed * game_framework.frame_time

        if self.isMM:
            self.ctime = get_time()
            if self.ctime - self.htime > 1:
                self.isMM = False

        if self.isXstop:
            self.xstop = 0
        else:
            self.xstop = 1


    def draw(self):
        self.cur_state.draw(self)
        # draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def getItem(self):
        self.S_i.play()
        self.life += 1
        self.ma2 = True

    def loseLife(self):
        self.life -= 1
        self.isMM = True
        self.htime = get_time()
        if self.life == 0:
            self.add_event(DEAD)
            self.S_d.play()
        if self.ma2 == True:
            self.ma2 = False
            self.S_i2.play()

    def fix(self, xx):
        self.fixX = xx

    def collide(self, b):
        left_a, bottom_a, right_a, top_a = self.get_bb()
        left_b, bottom_b, right_b, top_b = b.get_bb()

        if left_a > right_b: return False
        if right_a < left_b: return False
        if top_a < bottom_b: return False
        if bottom_a > top_b: return False
        return True

    def colBlock(self, b):
        left_a, bottom_a, right_a, top_a = self.get_bb()
        left_b, bottom_b, right_b, top_b = b.get_bb()

        if bottom_a == top_b: return True
        if top_a == bottom_b: return True
        if left_a == right_b: return True
        if right_a == left_b: return True
        return False

    def gameover(self):

        game_framework.change_state(gameover_state)