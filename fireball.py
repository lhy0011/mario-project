import random
from pico2d import *
import game_world
import game_framework
import main_state
import score


PIXEL_PER_METER = (10.0 / 0.3)
BALL_SPEED_KMPH = 100.0
BALL_SPEED_PPS = (BALL_SPEED_KMPH * 1000.0 / 60.0 / 60.0 * PIXEL_PER_METER)

class fireBall:
    image = None

    def __init__(self, x, y, dir):
        if fireBall.image == None:
            fireBall.image = load_image('resource/pngegg.png')
        self.y, self.dir = y, dir
        if dir < 0:
            self.x = x - 20
        else:
            self.x = x + 20
        self.speed = BALL_SPEED_PPS
        self.fixX = 0

        # self.S_s = load_music('sound/stomp.ogg')


    def get_bb(self):
        # fill here
        return self.x - 5, self.y - 5, self.x + 5, self.y + 5

    def draw(self):
        self.image.draw(self.x, self.y)
        # fill here for draw
        draw_rectangle(*self.get_bb())

    def update(self):
        self.x += self.speed * game_framework.frame_time * self.dir

        # for goomba in main_state.goombas:
        #     if main_state.collide(fireBall,goomba):
        #         main_state.score.sco += 200
        #         main_state.goombas.remove(goomba)
        #         game_world.remove_object(goomba)

        if self.x < 25 or self.x > 1000 - 25:
            game_world.remove_object(self)

        for g in main_state.goombas:
            if self.collide(g):
                main_state.goombas.remove(g)
                game_world.remove_object(g)
                game_world.remove_object(self)
                # self.S_s.play()
                main_state.score.sco += 200
        if self.collide(main_state.mm):
            main_state.mm.remove()
            game_world.remove_object(main_state.mm)
            game_world.remove_object(self)
            main_state.score.sco += 400
        for i in game_world.all_objects2(2):
            if self.collide(i):
                game_world.remove_object(self)


    def stop(self):
        self.speed = 0

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