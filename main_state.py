import random
import json
import os

from pico2d import *
import game_framework
import game_world
import gameover_state
import map1

from timer import Timer
from mario import Mario
from monster import M, Mgoomba
from map import BG, Ground, Coin, Cloud, Item2
from score import Score

name = "MainState"

x = 0

#배경
bg = None
ground = None
cloud = None

coins = []
item2 = None

score = None
timer = None

player = None

#몬스터
m = None
goombas = []


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

    # if int(left_a) == int(right_b) or int(right_a) == int(left_b) or left_a < right_b or right_b > left_b:
    #     isDead = True
    # else:
    #     isKill = True

    if int(top_b) == int(bottom_a) or int(top_b) > int(bottom_a):
        isKill = True
    else:
        isDead = True

    return True


def enter():

    global bg
    bg = BG()
    game_world.add_object(bg, 0)

    global ground
    ground = Ground()
    game_world.add_object(ground, 1)

    global cloud
    cloud = Cloud()
    game_world.add_object(cloud, 1)

    global coins
    coins = [Coin(map1.Map1.coin[i]) for i in range(3)]
    game_world.add_objects(coins, 2)

    global item2
    item2 = Item2()
    game_world.add_object(item2, 2)

    global m
    m = M()
    game_world.add_object(m, 2)

    global goombas
    goombas = [Mgoomba(map1.Map1.goomba[i]) for i in range(3)]
    game_world.add_objects(goombas, 2)

    global timer
    timer = Timer()
    game_world.add_object(timer, 2)

    global score
    score = Score()
    game_world.add_object(score, 2)

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
    global x, isKill, isDead

    for game_object in game_world.all_objects():
        game_object.update()

    xx = player.get_MX()
    if xx > x + 500:
        x = xx - 500
    for game_object in game_world.all_objects():
        game_object.fix(x)


    if collide(player, item2):
        player.ma2 = True
        game_world.remove_object(item2)


    for coin in coins:
        if collide(player, coin):
            score.coin += 1
            score.sco += 100
            coins.remove(coin)
            game_world.remove_object(coin)

    # 몬스터와 충돌체크

    for goomba in goombas:
        if Mcollide(player, goomba):
            if isKill == True:
                score.sco += 200
                goombas.remove(goomba)
                game_world.remove_object(goomba)
                isKill = False
            elif isDead == True:
                player.loseLife()
                timer.stop()


    if Mcollide(player, m):
        if isKill == True:
            score.sco += 200
            m.remove()
            game_world.remove_object(m)
            # isKill = False
        elif isDead == True:
            player.loseLife()
            timer.stop()
            pass

    if player.isdeadM:
        delay(2)
        game_framework.change_state(gameover_state)

    # if Mcollide(player.Mario.fireball.ball, goomba):
    #     game_world.remove_object(goomba)




def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()





