import random
from pico2d import *
import game_world
import game_framework
import server
import Elesis

class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(100, server.background.w - 100), random.randint(100, server.background.h - 100)

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        sx, sy = self.x - server.background.window_left, self.y - server.background.window_bottom
        self.image.draw(sx, sy)

    def update(self):
        pass

    def handle_collision(self, other, group):
            game_world.remove_object(self)


