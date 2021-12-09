import random
import json
import os

from pico2d import *
import game_framework
import game_world
import gameover_state
import map1

import sound
from timer import Timer
from mario import Mario, IdleState
from monster import M, Mgoomba
from map import BG, Block, Grounds, Coin, Cloud, Item2, RandBoxC, RandBoxI, Pipe1, Pipe2, Block2, RandBoxC2
from score import Score

name = "MainState"

x = 0

#배경

bg = None
ground = None
grounds = []
cloud = None
blocks = []
blocks2 = []

pipes1 = []
pipes2 = []

rboxsC = []
rboxsC2 = []
rboxsI = []

coins = []
item2 = None

score = None
timer = None

player = None

#몬스터
mm = None
goombas = []




def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True

def collideB(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if bottom_a >= top_b: return True

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

    # global ground
    # ground = Ground()
    # game_world.add_object(ground, 1)

    global grounds
    grounds = [Grounds(map1.Map1.ground[i]) for i in range(len(map1.Map1.ground))]
    game_world.add_objects(grounds, 1)

    # global grounds
    # grounds = [map1.Map1.ground[i] for i in range(len(map1.Map1.ground))]
    # game_world.add_object(grounds, 2)

    global cloud
    cloud = Cloud()
    game_world.add_object(cloud, 1)

    global coins
    coins = [Coin(map1.Map1.coin[i]) for i in range(3)]
    game_world.add_objects(coins, 2)

    # global item2
    # item2 = Item2()
    # game_world.add_object(item2, 2)

    global mm
    mm = M(map1.Map1.m[0])
    game_world.add_object(mm, 3)

    global goombas
    goombas = [Mgoomba(map1.Map1.goomba[i]) for i in range(len(map1.Map1.goomba))]
    game_world.add_objects(goombas, 3)

    global timer
    timer = Timer(300 + get_time())
    game_world.add_object(timer, 1)

    global score
    score = Score()
    game_world.add_object(score, 1)

    global player
    player = Mario()
    game_world.add_object(player, 3)

    global blocks
    blocks = [Block(map1.Map1.block[i]) for i in range(len(map1.Map1.block))]
    game_world.add_objects(blocks, 2)

    global blocks2
    blocks2 = [Block2(map1.Map1.block2_1[i], map1.Map1.block2_2[i]) for i in range(len(map1.Map1.block2_1))]
    game_world.add_objects(blocks2, 2)

    global pipes1
    pipes1 = [Pipe1(map1.Map1.pipe1[i]) for i in range(len(map1.Map1.pipe1))]
    game_world.add_objects(pipes1, 2)

    global pipes2
    pipes2 = [Pipe2(map1.Map1.pipe2[i]) for i in range(len(map1.Map1.pipe2))]
    game_world.add_objects(pipes2, 2)

    global rboxsC
    rboxsC = [RandBoxC(map1.Map1.randomboxC[i]) for i in range(len(map1.Map1.randomboxC))]
    game_world.add_objects(rboxsC, 2)

    global rboxsC2
    rboxsC2 = [RandBoxC2(map1.Map1.randomboxC2[i]) for i in range(len(map1.Map1.randomboxC2))]
    game_world.add_objects(rboxsC2, 2)

    global rboxsI
    rboxsI = [RandBoxI(map1.Map1.randomboxI[i]) for i in range (len(map1.Map1.randomboxI))]
    game_world.add_objects(rboxsI, 2)




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

    for g in grounds:
        if collide(player, g):
            if player.y >= g.y:
                player.y = g.y + 34
                player.curY = player.y


    for rc in rboxsC:
        if collide(player, rc):
            if player.y >= rc.y:
                player.y = rc.y + 35
                player.curY = player.y
            elif player.y <= rc.y + 5:
                player.y -= 20
                player.isJump = False
                player.isDescend = True
                if rc.isBreak == False:
                    score.sco += 100
                    score.coin += 1
                rc.isBreak = True
    for rc in rboxsC2:
        if collide(player, rc):
            if player.y >= rc.y:
                player.y = rc.y + 35
                player.curY = player.y
            elif player.y <= rc.y + 5:
                player.y -= 20
                player.isJump = False
                player.isDescend = True
                rc.isBreak = True
                rc.hitC -= 1
                if rc.hitC > 0:
                    rc.S_b.play()
                    score.sco += 100
                    score.coin += 1
    for r in rboxsI:
        if collide(player, r):
            if player.y >= r.y:
                player.y = r.y + 35
                player.curY = player.y
            elif player.y <= r.y + 5:
                player.y -= 20
                player.isJump = False
                player.isDescend = True
                r.isBreak = True

    for b in blocks:
        if collide(player, b):
            if player.y >= b.y:
                player.y = b.y + 35
                player.curY = player.y
            elif player.y <= b.y + 5:
                player.y -= 20
                player.isJump = False
                player.isDescend = True

    for p in pipes1:
        if collide(player, p):
            if player.y >= p.y:
                player.y = p.y + 55
                player.curY = player.y
                player.isXstop = False
            # elif (player.x - 17 >= p.x + 37 or player.x + 17 <= p.x + 37) and player.y < p.y:
            #     player.isXstop = True
            # else:
            #     player.isXtop = False
    for p in pipes2:
        if collide(player, p):
            if player.y >= p.y:
                player.y = p.y + 90
                player.curY = player.y
                player.isXstop = False

    for b in blocks2:
        if collide(player, b):
            if player.y >= b.y:
                player.y = b.y + 35
                player.curY = player.y


    for i in game_world.all_objects2(4):
        if collide(player, i):
            player.getItem()
            score.sco += 500
            i.remove()
            game_world.remove_object(i)


    for coin in coins:
        if collide(player, coin):
            score.coin += 1
            score.sco += 100
            coin.remove()
            game_world.remove_object(coin)

    # 몬스터와 충돌체크

    for goomba in goombas:
        if collide(player, goomba):
            if player.y-17 >= goomba.y+17:
                player.y += 15
                score.sco += 200
                goomba.S_d.play()
                goomba.isDead = True
                goombas.remove(goomba)
                game_world.remove_object(goomba)
                goomba.remove()
            else:
                if player.isMM == False:
                    player.loseLife()



            # if isKill == True:
            #     score.sco += 200
            #     goombas.remove(goomba)
            #     game_world.remove_object(goomba)
            #     isKill = False
            # elif isDead == True:
            #     player.loseLife()
            #     timer.stop()


    if Mcollide(player, mm):
        if isKill == True:
            score.sco += 200
            mm.remove()
            game_world.remove_object(mm)
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






