import framework
import map
import monster
import sound
import mario
from pico2d import *

open_canvas()

def enter():
    pass

p = mario.Mario() #플레이어 캐릭터
s = sound.BGM() #소리
bg = map.BG() #배경
g = map.Ground() #타일
goomba = monster.Mgoomba() #몬스터
mai = monster.M()

while mario.MOVING:
    clear_canvas()
    bg.drawBG()
    g.drawGround()
    mario.cmove()
    p.update()
    goomba.update()
    mai.update()
    goomba.draw()
    p.draw()
    mai.draw()
    update_canvas()
    delay(0.01)



def exit():
    global boy, grass
    del(boy)
    del(grass)


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            framework.quit()



def update():
    boy.update()


def draw():
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()

