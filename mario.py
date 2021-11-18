import game_framework
from pico2d import *
from fireball import fireBall

import game_world
import gameover_state

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 40.0  # Km / Hour
RUN_SPEED_PPS = (RUN_SPEED_KMPH * 1000.0 / 60.0 / 60.0 * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

JUMP_MAX_SPEED = 5
JUMP_MIN_SPEED = 2
JUMP_GRAVITY = 0.05

basicY = 83
MAXSPEED = 5
MAXHEIGHT = 250 # 점프높이
frameS = 0


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
            mario.curY = mario.y

        if event == D_DOWN:
            if mario.ma2:
                mario.fireball()
        pass

    def do(mario):
        if mario.isJump == True:
            if mario.jumpSpeed > JUMP_MIN_SPEED:
                mario.y += mario.jumpSpeed
                mario.jumpSpeed -= JUMP_GRAVITY
            else:
                mario.y += mario.jumpSpeed
        if mario.y > (basicY + MAXHEIGHT):
            mario.isDescend = True
            mario.isJump = False
        if mario.isJump == False and mario.isDescend == True:
            if mario.jumpSpeed < JUMP_MAX_SPEED:
                mario.y -= mario.jumpSpeed
                mario.jumpSpeed += JUMP_GRAVITY
            else:
                mario.y -= mario.jumpSpeed
            if int(mario.y) <= basicY:
                mario.isDescend = False
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
                else:
                    mario.marioL.draw(mario.x - mario.fixX, mario.y)

class RunState:
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
        #mario.dir = clamp(-1, mario.velocity, 1)

    def exit(mario, event):
        if event == A_DOWN:
            mario.isJump = True
            mario.jumpSpeed = JUMP_MAX_SPEED
            mario.curY = mario.y
        if event == D_DOWN:
            if mario.ma2:
                mario.fireball()
        pass

    def do(mario):
        mario.frame = (mario.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        mario.x += mario.velocity * game_framework.frame_time
        # mario.x = clamp(25, mario.x, 500)
        if mario.isJump == True:
            if mario.jumpSpeed > JUMP_MIN_SPEED:
                mario.y += mario.jumpSpeed
                mario.jumpSpeed -= JUMP_GRAVITY
            else:
                mario.y += mario.jumpSpeed
        if mario.y > (basicY + MAXHEIGHT):
            mario.isDescend = True
            mario.isJump = False
        if mario.isJump == False and mario.isDescend == True:
            if mario.jumpSpeed < JUMP_MAX_SPEED:
                mario.y -= mario.jumpSpeed
                mario.jumpSpeed += JUMP_GRAVITY
            else:
                mario.y -= mario.jumpSpeed
            if int(mario.y) <= basicY:
                mario.isDescend = False

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
                else:
                    mario.marioRL.clip_draw(int(mario.frame) * 36, 0, 36, 34, mario.x - mario.fixX, mario.y)


class CrouchState: #수정필요
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
        pass

    def do(mario):
        if mario.isJump == True:
            pass #(점프내용 구현)
        pass

    def draw(mario):
        if mario.dir == 1:
            if mario.isJump == True:
                mario.marioJR.draw(mario.x - mario.fixX, mario.y)
            else:
                mario.marioR.draw(mario.x - mario.fixX, mario.y)
        else:
            if mario.isJump == True:
                mario.marioJL.draw(mario.x - mario.fixX, mario.y)
            else:
                mario.marioL.draw(mario.x - mario.fixX, mario.y)


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
        self.x = 400
        self.y = basicY
        self.font = load_font('ENCR10B.TTF', 16)
        self.curY = 0

        self.isJump = False
        self.jumpSpeed= JUMP_MAX_SPEED
        self.jumpTimer = 0
        self.isDescend = False
        self.isdeadM = False
        self.ma2 = False

        self.life = 1

        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        self.fixX = 0

    def add_event(self, event):
        self.event_que.insert(0, event)

    def fireball(self):
        ball = fireBall(self.x - self.fixX, self.y, self.dir)
        game_world.add_object(ball, 1)

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

    def draw(self):
        self.cur_state.draw(self)
        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def loseLife(self):
        self.life -= 1
        if self.life == 0:
            self.add_event(DEAD)

    def fix(self, xx):
        self.fixX = xx

    def gameover(self):

        game_framework.change_state(gameover_state)