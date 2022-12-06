from pico2d import *
import game_world
import game_framework
from gonegg import GonEgg
import server
import Elesis

PIXEL_PER_METER = (10.0 / 0.1)  # 10 pixel 10 cm
RUN_SPEED_KMPH = 15.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.25
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 2
BOSS_PER_ACTION = 1

class Gon:
    image = None
    egg_time = 0.0

    def __init__(self, x, y, dir):
        if Gon.image == None:
            Gon.image = load_image('Gon_right.png')
        self.x, self.y, self.dir = x, y, dir
        self.w = self.image.w
        self.h = self.image.h
        self.font = load_font('ENCR10B.TTF', 16)
        self.hp = 100000

    #
    # def throw_egg(self):
    #     print('THROW_EGG')
    #     egg = GonEgg(self.x, self.y, self.dir * 10)
    #     game_world.add_object(egg, 1)

    def update(self):
        if server.gon.x < server.boy.x:
            self.dir = 1
        else:
            self.dir = -1
        self.x += self.dir * 0.3
        if Gon.egg_time > 3.0:
            Gon.egg_time = 0
        # delay(0.01)
        if Gon.egg_time == 0:
            server.gonegg = GonEgg(self.x, self.y, self.dir * 7)
            game_world.add_object(server.gonegg, 1)
            game_world.add_collision_pairs(server.gonegg, server.boy, 'boy:egg')
        Gon.egg_time += 0.01
        if self.hp <= 0:
            game_world.remove_object(self)
            server.boy.kill_score += 1
        pass

    def draw(self):
        sx, sy = self.x - server.background.window_left, self.y - server.background.window_bottom
        self.font.draw(sx - 40, sy + 80, '%d' % (self.hp), (255, 255, 0))

        if self.dir >= 0:
            self.image.draw(sx, sy, 100, 100)
        else:
            self.image.clip_composite_draw(0, 0, 162, 200, 3.14159, 'v', sx, sy, 100, 100)
        # draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - server.background.window_left - 50, self.y - server.background.window_bottom - 50, self.x + server.background.window_bottom + 50, self.y + server.background.window_bottom + 50

    def handle_event(self, event):
        pass

    def handle_collision(self, other, group):       # 충돌체크
        # game_world.remove_object(self)
        if group == 'fire:gon':
            self.hp -= 100


class Gorgon:
    image = None

    def __init__(self, x, y, dir):
        if Gorgon.image == None:
            Gorgon.image = load_image('Gorgon_animation_sheet.png')
        self.atk = False
        self.x, self.y, self.dir = x, y, dir
        self.x_velocity, self.y_velocity = 0, 0
        self.frame = 0
        self.font = load_font('ENCR10B.TTF', 16)
        self.hp = 250000

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        if self.x - server.boy.x > 100 or self.x - server.boy.x < -100:
            self.atk=False
        if self.x < server.boy.x:
            self.x_velocity = 150
        elif self.x > server.boy.x:
            self.x_velocity = -150
        self.x += self.x_velocity * game_framework.frame_time
        self.x = clamp(50, self.x, server.background.w-1-50)
        self.y = clamp(50, self.y, server.background.h-1-50)
        if self.hp <= 0:
            game_world.remove_object(self)
            server.boy.kill_score += 1
        pass

    def draw(self):
        sx, sy = self.x - server.background.window_left, self.y - server.background.window_bottom

        self.font.draw(sx - 40, sy + 80, '%d' % (self.hp), (255, 255, 0))

        if self.atk == True:
            if self.x_velocity > 0:
                self.image.clip_draw(int(self.frame) * 320, 0, 320, 300, sx, sy + 50, 180, 180)
                self.dir = 1
            elif self.x_velocity < 0:
                self.image.clip_draw(int(self.frame) * 320, 300, 320, 300, sx, sy + 50, 180, 180)
                self.dir = -1
        elif self.x_velocity > 0:
            self.image.clip_draw(int(self.frame) * 320, 600, 320, 300, sx, sy + 50, 180, 180)
            self.dir = 1
        elif self.x_velocity < 0:
            self.image.clip_draw(int(self.frame) * 320, 900, 320, 300, sx, sy + 50, 180, 180)
            self.dir = -1



    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + server.background.window_bottom + 50, self.y + server.background.window_bottom + 50

    def handle_event(self, event):

        pass

    def handle_collision(self, other, group):       # 충돌체크
        # game_world.remove_object(self)
        if group == 'fire:gorgon':
            self.hp -= 110
        elif group == 'boy:gorgon':
            self.x_velocity = 50
            self.atk = True


class Gorgos:
    image = None
    die_sound = None
    def __init__(self, x, y, dir):
        if Gorgos.image == None:
            Gorgos.image = load_image('Gorgos_stand.png')
        self.atk = False
        self.x, self.y, self.dir = x, y, dir
        self.x_velocity, self.y_velocity = 50, 0
        self.frame = 0
        self.font = load_font('ENCR10B.TTF', 16)
        self.hp = 500000
        if Gorgos.die_sound is None:
            Gorgos.die_sound = load_wav('k_win.mp3')
            Gorgos.die_sound.set_volume(32)
    def update(self):
        if self.x - server.boy.x > 300 or self.x - server.boy.x < -300:
            self.atk = False
        if self.x < server.boy.x:
            self.x_velocity = 50 * (server.boy.kill_score+2)
        elif self.x > server.boy.x:
            self.x_velocity = -50 * (server.boy.kill_score+2)
        if self.atk is False:
            Gorgos.image = load_image('Gorgos_stand.png')
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        elif self.atk is True:
            Gorgos.image = load_image('Gorgos_atk_sheet.png')
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % (FRAMES_PER_ACTION*2)
            self.x_velocity = self.x_velocity / 2
        self.x += self.x_velocity * game_framework.frame_time
        self.x = clamp(50, self.x, server.background.w-1-50)
        self.y = clamp(50, self.y, server.background.h-1-50)
        if self.hp <= 0:
            Gorgos.die_sound.play()
            game_world.remove_object(self)

        pass

    def draw(self):
        sx, sy = self.x - server.background.window_left, self.y - server.background.window_bottom

        self.font.draw(sx - 40, sy + 500, 'Gorgos : %d' % (self.hp), (255, 255, 0))

        if self.atk == True:
            self.image.clip_draw(int(self.frame) * 242, 0, 242, 258, sx, sy + 50, 550, 550)
            if self.x_velocity > 0:
                self.dir = 1
            elif self.x_velocity < 0:
                self.dir = -1
        elif self.x_velocity > 0:
            self.image.clip_draw(int(self.frame) * 300, 0, 300, 207, sx, sy + 100, 550, 550)
            self.dir = 1
        elif self.x_velocity < 0:
            self.image.clip_draw(int(self.frame) * 300, 207, 300, 207, sx, sy + 100, 550, 550)
            self.dir = -1



    def get_bb(self):
        return self.x - 150, self.y - 550, self.x + server.background.window_bottom + 150, self.y + server.background.window_bottom + 600

    def handle_event(self, event):

        pass

    def handle_collision(self, other, group):       # 충돌체크
        # game_world.remove_object(self)
        if group == 'fire:gorgos':
            self.hp -= 80
        elif group == 'boy:gorgos':
            self.x_velocity = 20
            self.atk = True