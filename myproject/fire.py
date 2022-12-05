from pico2d import *
import game_world
import server

class Fire():
    image = None

    def __init__(self, x, y, velocity):
        if Fire.image == None:
            Fire.image = load_image('sword_fire.png')
        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        sx, sy = self.x - server.background.window_left, self.y - server.background.window_bottom
        if self.velocity >= 0:
            self.image.draw(sx, sy, 100, 100)
        else:
            self.image.clip_composite_draw(0, 0, 948, 232, 3.14159, 'v', sx, sy, 100, 100)
    def update(self):
        self.x += self.velocity
