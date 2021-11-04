import map
import sound
import mario
from pico2d import *

open_canvas()


p = mario.Mario() #플레이어 캐릭터
s = sound.BGM() #소리
bg = map.BG() #배경
g = map.Ground() #타일
goomba = map.Mgoomba() #몬스터

while mario.MOVING:
    clear_canvas()
    bg.drawBG()
    g.drawGround()
    mario.cmove()
    p.update()
    goomba.update()
    goomba.draw()
    p.draw()
    update_canvas()
    delay(0.01)


close_canvas()
