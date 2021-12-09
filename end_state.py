import game_framework
from pico2d import *
import score

image = None
font = None

def enter():
    global image, font
    font = load_font('ENCR10B.TTF', 50)
    image = load_image('resource/game_over.png')


def exit():
    global image, font
    del(image)
    del(font)

import main_state

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_r):
                game_framework.change_state(main_state)

def draw():
    clear_canvas()
    image.clip_draw(50, 50, 50, 50, 500, 500, 1000, 1000)
    font.draw(250, 400, 'GAME CLEAR!', (255, 255, 255))
    font.draw(620, 260, 'SCORE', (255, 255, 255))
    font.draw(620, 210, '%d' % main_state.score.sco, (255, 255, 255))
    font.draw(180, 260, 'LEFT TIME', (255, 255, 255))
    font.draw(180, 210, '%d' % main_state.timer.leftT, (255, 255, 255))

    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass