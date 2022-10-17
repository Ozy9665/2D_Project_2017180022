import pico2d
import game_framework
import title_state

player = None
background = None
boss = None


class BackGround:
    def __init__(self):
        self.land_image = pico2d.load_image('land_before.png')
        self.back_image = pico2d.load_image('TheCave.png')

    def draw(self):
        # self.image.draw(400, 20)
        self.back_image.draw(720, 506)
        for x in range(200, 1200 + 1, 200):
            self.land_image.draw(x, 20)


class Player:
    def __init__(self):
        self.x, self.y = 90, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = pico2d.load_image('elesis_animation.png')
        self.item = None
        self.attacking = 0
        self.atk_time = 0.0

    def update(self):
        # self.frame = (self.frame + 1) % 8
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
                self.image.clip_draw(0, 37, 210, 118, self.x, self.y)
            elif self.dir == 1:
                self.image.clip_draw(210, 37, 210, 118, self.x, self.y)
            else:
                if self.face_dir == 1:
                    self.image.clip_draw(210, 37, 210, 118, self.x, self.y)
                else:
                    self.image.clip_draw(0, 37, 210, 118, self.x, self.y)
        elif self.dir == -1:
            self.image.clip_draw(0, 156, 175, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(175, 156, 175, 100, self.x, self.y)
        else:
            if self.face_dir == 1:
                self.image.clip_draw(152, 253, 152, 118, self.x, self.y)
            else:
                self.image.clip_draw(0, 253, 152, 118, self.x, self.y)


class Boss:
    global player

    def __init__(self):
        self.x, self.y = 1100, 140
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.left_image = pico2d.load_image('Gorgos_left.png')
        self.right_image = pico2d.load_image('Gorgos_right.png')
        self.attack_image = None

    def update(self):
        # self.frame = (self.frame + 1) % 8
        if -500 < (player.x - self.x) < 500:
            self.x += self.dir * 0.5
        self.x = pico2d.clamp(250, self.x, 1200)

    def draw(self):
        if player.x >= self.x:
            self.dir = 1
            self.right_image.draw(self.x, self.y)
        elif player.x < self.x:
            self.dir = -1
            self.left_image.draw(self.x, self.y)


def enter():
    global player, background, boss
    player = Player()
    boss = Boss()
    background = BackGround()


def exit():
    global player, background, boss
    del player
    del background
    del boss


def update():
    player.update()
    boss.update()


def draw():
    pico2d.clear_canvas()
    draw_world()
    pico2d.update_canvas()


def draw_world():
    background.draw()
    player.draw()
    boss.draw()


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



