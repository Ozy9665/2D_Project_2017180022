import pico2d
import game_framework
import item_state
import title_state


class Grass:
    def __init__(self):
        self.image = pico2d.load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = pico2d.load_image('animation_sheet.png')
        self.ball_image = pico2d.load_image('ball21x21.png')
        self.big_ball_image = pico2d.load_image('ball41x41.png')
        self.item = None

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir * 1
        self.x = pico2d.clamp(0, self.x, 800)

    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        else:
            if self.face_dir == 1:
                self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
            else:
                self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)

        if self.item == 'BigBall':
            self.big_ball_image.draw(self.x + 10, self.y + 50)
        elif self.item == 'Ball':
            self.ball_image.draw(self.x + 10, self.y + 50)

def enter():
    global boy, grass, running
    boy = Boy()
    grass = Grass()
    running = True


def exit():
    global boy, grass
    del boy
    del grass


def update():
    boy.update()


def draw_world():
    grass.draw()
    boy.draw()


def draw():
    pico2d.clear_canvas()
    draw_world()
    pico2d.update_canvas()



def handle_events():
    events = pico2d.get_events()
    for event in events:
        if event.type == pico2d.SDL_QUIT:
            game_framework.quit()
        elif event.type == pico2d.SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.change_state(title_state)
                case pico2d.SDLK_i:
                    game_framework.push_state(item_state)
                case pico2d.SDLK_LEFT:
                    boy.dir -= 1
                case pico2d.SDLK_RIGHT:
                    boy.dir += 1
        elif event.type == pico2d.SDL_KEYUP:
            match event.key:
                case pico2d.SDLK_LEFT:
                    boy.dir += 1
                    boy.face_dir = -1
                case pico2d.SDLK_RIGHT:
                    boy.dir -= 1
                    boy.face_dir = 1


def pause():
    pass


def resume():
    pass


boy = None
grass = None
running = None

# open_canvas()
#
# enter()
#
# # game main loop code
# while running:
#     handle_events()
#     update()
#     draw()
# exit()
# # finalization code
# close_canvas()
