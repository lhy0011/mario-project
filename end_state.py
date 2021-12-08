import game_framework
from pico2d import *

image = None
font = None

def enter():
    global image, font
    font = load_font('ENCR10B.TTF', 40)
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
    image.draw(500, 300, 1000, 600)

    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass