from pico2d import *
import game_framework
import title_state

class Land:
    def __init__(self):
        self.image = load_image('land_before.png')

    def draw(self):
        self.image.draw(400, 30)