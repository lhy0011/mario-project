import map
import sound
import mario
from pico2d import *

open_canvas()


p = mario.Mario()
s = sound.BGM()
bg = map.BG()
g = map.Ground()


while mario.MOVING:
    clear_canvas()
    bg.drawBG()
    g.drawGround()
    mario.cmove()
    p.update()
    p.draw()
    update_canvas()
    delay(0.01)


close_canvas()
