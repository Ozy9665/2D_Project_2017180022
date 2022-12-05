import game_framework
from pico2d import *
from fire import Fire

import game_world
import server
# 한 픽셀당 크기
# Elesis Run Speed
# Elesis height
PIXEL_PER_METER = (10.0 / 0.1)  # 10 pixel 10 cm
RUN_SPEED_KMPH = 15.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.25
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4



# Boy Event
RIGHTKEY_DOWN, LEFTKEY_DOWN, UPKEY_DOWN, DOWNKEY_DOWN, RIGHTKEY_UP, LEFTKEY_UP, DOWNKEY_UP, Z_DOWN = range(8)
# UPKEY_UP

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHTKEY_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFTKEY_DOWN,
    (SDL_KEYDOWN, SDLK_UP): UPKEY_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): DOWNKEY_DOWN,
    (SDL_KEYDOWN, SDLK_z): Z_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHTKEY_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFTKEY_UP,
    # (SDL_KEYUP, SDLK_UP): UPKEY_UP,
    (SDL_KEYUP, SDLK_DOWN): DOWNKEY_UP
}


# Boy States
# class AtkState:
#
#     def enter(boy, event):
#         if event == RIGHTKEY_DOWN:
#             boy.x_velocity += RUN_SPEED_PPS
#         elif event == RIGHTKEY_UP:
#             boy.x_velocity -= RUN_SPEED_PPS
#         if event == LEFTKEY_DOWN:
#             boy.x_velocity -= RUN_SPEED_PPS
#         elif event == LEFTKEY_UP:
#             boy.x_velocity += RUN_SPEED_PPS
#         if event == Z_DOWN:
#             pass
#
#         if event == UPKEY_DOWN:
#             if boy.landing:
#                 boy.y += 10
#                 boy.jp = -900
#                 boy.gravity = 1
#                 boy.landing = False
#             else:
#                 pass
#         # elif event == UPKEY_UP:
#         #     boy.y_velocity -= RUN_SPEED_PPS
#         # if event == DOWNKEY_DOWN:
#         #     boy.y_velocity -= RUN_SPEED_PPS
#         # elif event == DOWNKEY_UP:
#         #     boy.y_velocity += RUN_SPEED_PPS
#
#
#
#     def exit(boy, event):
#         pass
#
#     def do(boy):
#         boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
#         boy.x += boy.x_velocity * game_framework.frame_time
#         boy.y_velocity = boy.gravity + boy.jp
#         boy.y -= boy.y_velocity * game_framework.frame_time
#         boy.x = clamp(50, boy.x, server.background.w-1-50)
#         boy.y = clamp(50, boy.y, server.background.h-1-50)
#
#         # speed
#         if boy.landing == False:
#             boy.gravity += 2
#             boy.jp += 10
#         elif boy.landing:
#             boy.jp = 0
#
#
#
#
#
#     def draw(boy):
#         sx, sy = boy.x - server.background.window_left, boy.y - server.background.window_bottom
#
#         boy.font.draw(sx - 40, sy + 40, '%d' % (boy.ballCount), (255, 255, 0))
#
#         if boy.x_velocity > 0:
#             boy.image.clip_draw(int(boy.frame) * 330, 230, 330, 230, sx, sy, 163, 163)
#             boy.dir = 1
#         elif boy.x_velocity < 0:
#             boy.image.clip_draw(int(boy.frame) * 330, 0, 330, 230, sx, sy, 163, 163)
#             boy.dir = -1
#         else:
#             # if boy x_velocity == 0
#             if boy.y_velocity > 0 or boy.y_velocity < 0:
#                 if boy.dir == 1:
#                     boy.image.clip_draw(int(boy.frame) * 330, 230, 330, 230, sx, sy, 163, 163)
#                 else:
#                     boy.image.clip_draw(int(boy.frame) * 330, 0, 330, 230, sx, sy, 163, 163)
#             else:
#                 # boy is idle
#                 if boy.dir == 1:
#                     boy.image.clip_draw(int(boy.frame) * 330, 690, 330, 230, sx, sy, 163, 163)
#                 else:
#                     boy.image.clip_draw(int(boy.frame) * 330, 460, 330, 230, sx, sy, 163, 163)


class WalkingState:

    def enter(boy, event):
        if event == RIGHTKEY_DOWN:
            boy.x_velocity += RUN_SPEED_PPS
        elif event == RIGHTKEY_UP:
            boy.x_velocity -= RUN_SPEED_PPS
        if event == LEFTKEY_DOWN:
            boy.x_velocity -= RUN_SPEED_PPS
        elif event == LEFTKEY_UP:
            boy.x_velocity += RUN_SPEED_PPS
        if event == Z_DOWN:
            pass

        if event == UPKEY_DOWN:
            if boy.landing:
                boy.y += 10
                boy.jp = -1000
                boy.gravity = 1
                boy.landing = False
            else:
                pass
        # elif event == UPKEY_UP:
        #     boy.y_velocity -= RUN_SPEED_PPS
        if event == DOWNKEY_DOWN:
            boy.jp += 500
        # elif event == DOWNKEY_UP:
        #     boy.y_velocity += RUN_SPEED_PPS



    def exit(boy, event):
        if event == Z_DOWN:
            boy.sword_fire()
        pass

    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        boy.x += boy.x_velocity * game_framework.frame_time
        boy.y_velocity = boy.gravity + boy.jp
        boy.y -= boy.y_velocity * game_framework.frame_time
        boy.x = clamp(50, boy.x, server.background.w-1-50)
        boy.y = clamp(50, boy.y, server.background.h-1-50)

        # speed
        if boy.landing == False:
            boy.gravity += 2
            boy.jp += 10
        elif boy.landing:
            boy.jp = 0





    def draw(boy):
        sx, sy = boy.x - server.background.window_left, boy.y - server.background.window_bottom

        boy.font.draw(sx - 40, sy + 80, '%d' % (boy.hp), (255, 255, 0))

        if boy.x_velocity > 0:
            boy.image.clip_draw(int(boy.frame) * 330, 230, 330, 230, sx, sy, 163, 163)
            boy.dir = 1
        elif boy.x_velocity < 0:
            boy.image.clip_draw(int(boy.frame) * 330, 0, 330, 230, sx, sy, 163, 163)
            boy.dir = -1
        else:
            # if boy x_velocity == 0
            if boy.y_velocity > 0 or boy.y_velocity < 0:
                if boy.dir == 1:
                    boy.image.clip_draw(int(boy.frame) * 330, 230, 330, 230, sx, sy, 163, 163)
                else:
                    boy.image.clip_draw(int(boy.frame) * 330, 0, 330, 230, sx, sy, 163, 163)
            else:
                # boy is idle
                if boy.dir == 1:
                    boy.image.clip_draw(int(boy.frame) * 330, 690, 330, 230, sx, sy, 163, 163)
                else:
                    boy.image.clip_draw(int(boy.frame) * 330, 460, 330, 230, sx, sy, 163, 163)


next_state_table = {
    WalkingState: {RIGHTKEY_UP: WalkingState, LEFTKEY_UP: WalkingState, RIGHTKEY_DOWN: WalkingState, LEFTKEY_DOWN: WalkingState,
                Z_DOWN: WalkingState, UPKEY_DOWN: WalkingState, DOWNKEY_UP: WalkingState, DOWNKEY_DOWN: WalkingState}
}


class Boy:

    def __init__(self):
        # Boy is only once created, so instance image loading is fine
        self.landing = False
        self.gravity = 1
        self.jp = 0
        self.image = load_image('elesis_animation_sheet.png')
        self.ballCount = 0
        self.font = load_font('ENCR10B.TTF', 16)
        self.hp, self.mp = 1000, 0
        self.dir = 1
        self.x_velocity, self.y_velocity = 0, 0
        self.frame = 0
        self.event_que = []
        self.cur_state = WalkingState
        self.cur_state.enter(self, None)
        # self.x, self.y = get_canvas_width() // 2, get_canvas_height() // 2
        # self.x, self.y = server.background.w // 2, server.background.h // 2
        self.x, self.y = 500, 300

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def set_background(self, bg):
        self.bg = bg
        self.x = self.bg.w / 2
        self.y = self.bg.h / 2

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)



    def draw(self):
        self.cur_state.draw(self)

    def sword_fire(self):
        print('SWORD FIRE')
        fire = Fire(self.x, self.y, self.dir * 10)
        game_world.add_object(fire, 1)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def handle_collision(self, other, group):       # 충돌체크
        if group == 'boy:land':
            if self.y > other.y and self.landing == False:
                # print('she is landing')
                self.landing = True
                self.gravity = 0
                self.jp = 0
