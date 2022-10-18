from pico2d import *
import pygame
import logo_state
import game_framework
import play_state

image = None
ps_image = None     # press start


def enter():
    global image, ps_image
    image = load_image('Elesis_Title.png')
    ps_image = load_image('press_start_rem.png')


def exit():
    global image, ps_image
    del image
    del ps_image


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.change_state(logo_state)
            elif event.key == SDLK_SPACE:
                game_framework.change_state(play_state)


def draw():
    clear_canvas()
    image.draw(720, 505)
    ps_image.draw(720, 200)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass


