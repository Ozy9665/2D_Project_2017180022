from pico2d import *
import game_framework
import title_state

logo_image = None
background_image = None
logo_time = 0.0


def enter():
    global logo_image, background_image
    logo_image = load_image('그체 로고.png')
    background_image = load_image('WhiteBackground.png')


def exit():
    global logo_image, background_image
    del logo_image, background_image


def update():
    global logo_time
    if logo_time > 5.0:
        logo_time = 0
        game_framework.change_state(title_state)
    delay(0.01)
    logo_time += 0.01


def draw():
    clear_canvas()
    background_image.draw(700, 512)
    logo_image.draw(700, 512)
    update_canvas()


def handle_events():
    events = get_events()
