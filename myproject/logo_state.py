import title_state
import play_state
import game_framework
from pico2d import *
from background import FixedBackground as Background
running = True
image = None
logo_time = 0.0


def enter():
    global image
    image = load_image('realLogo.png')
    image.bgm = load_music('logo.mp3')
    image.bgm.set_volume(32)
    image.bgm.repeat_play()
    pass

def exit():
    global image
    del image
    pass


def update():
    global logo_time
    delay(0.01)
    logo_time += 0.01
    if logo_time > 3.0:
        logo_time = 0
        game_framework.change_state(title_state)



def draw():
    clear_canvas()
    image.draw(640, 400, 1280, 800)
    update_canvas()


def handle_events():
    events = get_events()

