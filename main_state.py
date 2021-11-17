import random
import json
import os

from pico2d import *
import game_framework
import game_world

from timer import Timer
from mario import Mario
from monster import M, Mgoomba
from map import BG, Ground

name = "MainState"

#배경
bg = None
ground = None


timer = None
player = None
#몬스터
m = None
goomba = None


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True


isDead = None
isKill = None

def Mcollide(a, b):
    global isKill, isDead
    left_a, bottom_a, right_a, top_a = a.get_bb() # 마리오
    left_b, bottom_b, right_b, top_b = b.get_bb() # 몬스터

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    # if :
    #     isKill = True
    # else:
    #     isDead = True

    return True


def enter():

    global bg
    bg = BG()
    game_world.add_object(bg, 0)

    global ground
    ground = Ground()
    game_world.add_object(ground, 1)

    global m
    m = M()
    game_world.add_object(m, 2)

    global goomba
    goomba = Mgoomba()
    game_world.add_object(goomba, 2)


    global timer
    timer = Timer()
    game_world.add_object(timer, 2)

    global player
    player = Mario()
    game_world.add_object(player, 3)






def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            player.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()


    if Mcollide(player, goomba):
        if isKill == True:
            # enemies.monster.remove(goomba)
            game_world.remove_object(goomba)
        elif isDead == True:
            player.loseLife()
            timer.stop()
            pass
    if Mcollide(player, m):
        if isKill == True:
            # enemies.monster.remove(m)
            game_world.remove_object(m)
        elif isDead == True:
            player.loseLife()
            timer.stop()
            pass



def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






