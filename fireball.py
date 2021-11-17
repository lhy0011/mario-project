import random
from pico2d import *
import game_world
import game_framework

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

    def get_bb(self):
        # fill here
        return self.x - 5, self.y - 5, self.x + 5, self.y +5

    def draw(self):
        self.image.draw(self.x, self.y)
        # fill here for draw
        draw_rectangle(*self.get_bb())

    def update(self):
        self.x += self.speed * game_framework.frame_time * self.dir

        if self.x < 25 or self.x > 1000 - 25:
            game_world.remove_object(self)

    def stop(self):
        self.speed = 0