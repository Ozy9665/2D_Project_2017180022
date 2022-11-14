from pico2d import *
# import game_world

# 1 : 이벤트 정의
RD, LD, RU, LU, TIMER, SPACE, JUMP, ATTACK, SWORDFIRE = range(9)    # 공격, 스킬, 점프 추가하기
event_name = ['RD', 'LD', 'RU', 'LU', 'TIMER', 'SPACE', 'JUMP', 'ATTACK', 'SWORDFIRE']

key_event_table = {
    (SDL_KEYDOWN, SDLK_SPACE): SPACE,
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU
    #    공격, 점프, 스킬 추가하기
    #    걷기는 고민 - c를 한 번 누르면 속도 낮추고, 이미지 바꾸기 등
}


# 2 : 상태의 정의
class IDLE:
    @staticmethod
    def enter(self, event):
        print('ENTER IDLE')
        self.dir = 0
        self.timer = 1000

    @staticmethod
    def exit (self, event):
        print('EXIT IDLE')
        # if event == SPACE:
        #     pass
        
    @staticmethod
    def do(self):
        # self.frame = 
        self.timer -= 1
        # if self.timer == 0:
        #     self.add_event(TIMER)
        
    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            # self.image.clip_draw()
            pass    # 계산 후 집어넣기
        else:
            # self.image.clip_draw()
            pass    # 계산 후 집어넣기


# 3 : 상태 변환 구현

next_state = {
    IDLE: {SPACE: IDLE}
}