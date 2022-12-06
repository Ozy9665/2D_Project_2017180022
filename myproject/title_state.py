from pico2d import *
import logo_state

import game_framework
import play_state

image = None

def enter():
    global image
    image = load_image('hope.jpg')
    image.bgm = load_music('hope.mp3')
    image.bgm.set_volume(32)
    image.bgm.repeat_play()

def exit():
    global image
    del image

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_state(play_state)
        elif event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()

def draw():
    clear_canvas()
    image.clip_draw(0, 0, 296, 170, 640, 400, 1280, 800)
    update_canvas()

def update():
    pass

def pause():
    pass

def resume():
    pass
