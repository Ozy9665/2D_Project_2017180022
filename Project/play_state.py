import pico2d
import game_framework
import title_state
import random

player = None
background = None
boss = None
gorgon = None
gon = None


class BackGround:
    def __init__(self):
        self.land_image = pico2d.load_image('land_before.png')
        self.back_image = pico2d.load_image('TheCave.png')

    def draw(self):
        # self.image.draw(400, 20)
        self.back_image.draw(720, 506)
        for x in range(200, 1200 + 1, 200):
            self.land_image.draw(x, 20)
        self.land_image.draw(-100, 200)
        self.land_image.draw(1300, 200)
        self.land_image.draw(300, 400)
        self.land_image.draw(1100, 400)
        self.land_image.draw(0, 600)
        self.land_image.draw(500, 600)
        self.land_image.draw(1200,600)


class Player:
    def __init__(self):
        self.x, self.y = 90, 100
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = pico2d.load_image('elesis_animation.png')
        self.item = None
        self.attacking = 0
        self.atk_time = 0.0

    def update(self):
        self.frame = (self.frame + 1) % 2
        self.x += self.dir * 2
        self.x = pico2d.clamp(0, self.x, 1440)
        if self.attacking == 1:
            if self.atk_time > 0.25:
                self.atk_time = 0.0
                self.attacking = 0
            else:
                self.atk_time += 0.01

    def draw(self):
        # self.image.draw(self.x, self.y)
        if self.attacking == 1:
            if self.dir == -1:
                self.image.clip_draw(0, 0, 222, 130, self.x, self.y)
            elif self.dir == 1:
                self.image.clip_draw(222, 0, 222, 130, self.x, self.y)
            else:
                if self.face_dir == 1:
                    self.image.clip_draw(222, 0, 222, 130, self.x, self.y)
                else:
                    self.image.clip_draw(0, 0, 222, 130, self.x, self.y)
        elif self.dir == -1:
            self.image.clip_draw(10 + self.frame * 170, 130, 170, 105, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(350 + self.frame * 170, 130, 170, 105, self.x, self.y)
        else:
            if self.face_dir == 1:
                self.image.clip_draw(160, 234, 160, 124, self.x, self.y)
            else:
                self.image.clip_draw(0, 234, 160, 124, self.x, self.y)


class Boss:
    global player

    def __init__(self):
        self.x, self.y = 1190, 140
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.left_image = pico2d.load_image('Gorgos_left.png')
        self.right_image = pico2d.load_image('Gorgos_right.png')
        self.attack_image = None

    def update(self):
        # self.frame = (self.frame + 1) % 8
        # if 10 < (player.x - self.x) < 10:
        #     pass
        if -500 < (player.x - self.x) < 500:
            if -60 < (player.x - self.x) < 60 and player.attacking == 1:
                self.left_image = None      # 사망처리
                self.right_image = None     # but 미완성
            self.x += self.dir * 0.4
        self.x = pico2d.clamp(250, self.x, 1200)

    def draw(self):
        if player.x >= self.x:
            self.dir = 1
            self.right_image.draw(self.x, self.y)
        elif player.x < self.x:
            self.dir = -1
            self.left_image.draw(self.x, self.y)


class Gorgon:
    global player

    def __init__(self):
        self.x, self.y = 600, 140
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.left_image = pico2d.load_image('Gorgon_left.png')
        self.right_image = pico2d.load_image('Gorgon_right.png')
        self.attack_image = None

    def update(self):
        # self.frame = (self.frame + 1) % 8
        if -400 < (player.x - self.x) < 400:
            if -30 < (player.x - self.x) < 30 and player.attacking == 1:
                self.left_image = None      # 사망처리
                self.right_image = None     # but 미완성
            self.x += self.dir * 0.6
        self.x = pico2d.clamp(250, self.x, 1200)

    def draw(self):
        if player.x >= self.x:
            self.dir = 1
            self.right_image.draw(self.x, self.y)
        elif player.x < self.x:
            self.dir = -1
            self.left_image.draw(self.x, self.y)


class Gon:
    global player

    def __init__(self):
        self.x, self.y = 400, 140
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.left_image = pico2d.load_image('Gon_left.png')
        self.right_image = pico2d.load_image('Gon_right.png')
        self.attack_image = None

    def update(self):
        # self.frame = (self.frame + 1) % 8
        if -300 < (player.x - self.x) < 300:
            if -30 < (player.x - self.x) < 30 and player.attacking == 1:
                self.left_image = None      # 사망처리
                self.right_image = None     # but 미완성
            self.x += self.dir * 0.8
        self.x = pico2d.clamp(250, self.x, 1200)

    def draw(self):
        if player.x >= self.x:
            self.dir = 1
            self.right_image.draw(self.x, self.y)
        elif player.x < self.x:
            self.dir = -1
            self.left_image.draw(self.x, self.y)


def enter():
    global player, background, boss, gorgon, gon
    player = Player()
    boss = Boss()
    gorgon = Gorgon()
    gon = Gon()
    background = BackGround()


def exit():
    global player, background, boss, gorgon, gon
    del player
    del background
    del gorgon
    del boss
    del gon


def update():
    player.update()
    boss.update()
    gorgon.update()
    gon.update()


def draw():
    pico2d.clear_canvas()
    draw_world()
    pico2d.update_canvas()


def draw_world():
    background.draw()
    player.draw()
    if boss.left_image != None:
        boss.draw()
    if gorgon.left_image != None:
        gorgon.draw()
    if gon.left_image != None:
        gon.draw()


def stop_atk():
    global player
    player.attacking = 0


def handle_events():
    global player
    events = pico2d.get_events()
    for event in events:
        if event.type == pico2d.SDL_QUIT:
            game_framework.quit()
        elif event.type == pico2d.SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.change_state(title_state)
                case pico2d.SDLK_z:
                    player.attacking = 1
                # case pico2d.SDLK_i:
                    # game_framework.push_state(item_state)
                case pico2d.SDLK_LEFT:
                    player.dir -= 1
                case pico2d.SDLK_RIGHT:
                    player.dir += 1
        elif event.type == pico2d.SDL_KEYUP:
            match event.key:
                case pico2d.SDLK_LEFT:
                    player.dir += 1
                    player.face_dir = -1
                case pico2d.SDLK_RIGHT:
                    player.dir -= 1
                    player.face_dir = 1
                # case pico2d.SDLK_z:
                #     player.attacking = 1


def pause():
    pass


def resume():
    pass



