from pico2d import *
import game_world
import game_framework
from gonegg import GonEgg
import server

PIXEL_PER_METER = (10.0 / 0.1)  # 10 pixel 10 cm
RUN_SPEED_KMPH = 15.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.25
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4

class Gon:
    image = None

    def __init__(self, x, y, dir):
        if Gon.image == None:
            Gon.image = load_image('Gon_right.png')
        self.x, self.y, self.dir = x, y, dir
        self.timer = 2.0
        self.w = self.image.w
        self.h = self.image.h

        self.hp = 500

    #
    # def throw_egg(self):
    #     print('THROW_EGG')
    #     egg = GonEgg(self.x, self.y, self.dir * 10)
    #     game_world.add_object(egg, 1)

    def update(self):
        # self.timer -= 0.1
        # if self.timer == 0:
        #     egg = GonEgg(self.x, self.y, self.dir * 3)
        #     game_world.add_object(egg, 1)
        pass

    def draw(self):
        sx, sy = self.x - server.background.window_left, self.y - server.background.window_bottom

        if self.dir >= 0:
            self.image.draw(sx, sy, 100, 100)
        else:
            self.image.clip_composite_draw(0, 0, 162, 200, 3.14159, 'v', sx, sy, 100, 100)

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def handle_event(self, event):
        pass

    def handle_collision(self, other, group):       # 충돌체크
        if group == 'fire:enemies':
            print('enemy hit fire')
            self.hp -= 100
            print(self.hp)
            if self.hp <= 0:
                game_world.remove_object(self)



