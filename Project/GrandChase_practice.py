from pico2d import *
import random


# 오브젝트 클래스


class Land:
    def __init__(self):
        self.image = load_image('land_before.png')

    def draw(self):
        self.image.draw(100, 25)
        self.image.draw(600, 25)
        self.image.draw(1100, 25)
        self.image.draw(1600, 25)


class Elesis:
    global dir

    def __init__(self):
        self.x, self.y = 700, 130
        self.image = load_image('엘리시스.png')

    def update(self):
        self.x += dir

    def draw(self):
        self.image.draw(self.x, self.y)

# character = load_image('Gorgos_right.png')
# character2 = load_image('Gorgos_left.png')
# mSlash = load_image('메가슬래쉬.png')
# sFire = load_image('소드파이어.png')
# cEx = load_image('크리티컬엑스.png')


# def draw_basic():
#     grass.draw(100, 50)      # 지면
#     grass.draw(600, 50)
#     mSlash.draw(50, 550)    # 스킬 아이콘
#     sFire.draw(120, 550)
#     cEx.draw(190, 550)

#
# def draw_character(character):  # 캐릭터 그리기
#     character.draw(x, 170)


def handle_events():
    global running, dir
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_RIGHT:
                dir += 1
            elif event.key == SDLK_LEFT:
                dir -= 1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1



open_canvas(1440, 1024)

# initialization code

land = Land()   # 지면 객체 생성
elesis = Elesis()
dir = 0
running = True

# Game main loop code
while running:
    handle_events()

    # 시뮬레이션
    elesis.update()

    # 렌더링 : 보여준다
    clear_canvas()
    land.draw()
    elesis.draw()
    update_canvas()


# finalization code

del land
del elesis

close_canvas()
