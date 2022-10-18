# MyGame

import pico2d
import game_framework
import logo_state   # 완성은 로고부터 시작
import play_state   # 테스트할 부분있으면 따로

pico2d.open_canvas(1440, 1012)
game_framework.run(play_state)
pico2d.close_canvas()