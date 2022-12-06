import random
import json
import os

from pico2d import *
import game_framework
import game_world

from ball import Ball
from Elesis import Boy
# fill here
from background import FixedBackground as Background
from background import GonLand1
# from background import TileBackground as Background
from enemies import Gon
from enemies import Gorgon
from enemies import Gorgos
import server
from zombie import Zombie


def enter():
    server.boy = Boy()
    game_world.add_object(server.boy, 1)
    server.background = Background()
    game_world.add_object(server.background, 0)

    server.gonland = GonLand1()
    game_world.add_object(server.gonland, 0)
    # gonland1 = [GonLand() for i in range(10)]
    # game_world.add_objects(gonland1, 1)
    # for gl in gonland1:
    #     x = 200
    #     gl.x += x
    #     x += 200



    server.gon = Gon(1500, 120, -1)
    game_world.add_object(server.gon, 1)

    server.gorgon = Gorgon(800, 110, -1)
    game_world.add_object(server.gorgon, 1)

    server.gorgos = Gorgos(2100, 200, -1)
    game_world.add_object(server.gorgos, 1)
    # server.gorgos = Gorgos(1600, 200, -1)
    # game_world.add_object(server.gorgos, 1)

    # server.ball = [Ball() for i in range(100)]
    # ball_list = [Ball() for i in range(100)]
    # game_world.add_objects(ball_list, 1)

    # 충돌 그룹 관리
    # game_world.add_collision_pairs(server.boy, ball_list, 'boy:ball')
    game_world.add_collision_pairs(server.boy, server.gonland, 'boy:land')
    # game_world.add_collision_pairs(server.fire, server.gon, 'fire:gon')
    game_world.add_collision_pairs(None, server.gon, 'fire:gon')
    game_world.add_collision_pairs(server.boy, server.gorgon, 'boy:gorgon')
    game_world.add_collision_pairs(server.boy, server.gorgos, 'boy:gorgos')
    # game_world.add_collision_pairs(server.boy, server.gorgos, 'boy:gorgos')
    # game_world.add_collision_pairs(server.boy, server.gon, 'boy:gon')
    # game_world.add_collision_pairs(server.gorgon, server.fire, 'fire:gorgon')

def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            server.boy.handle_event(event)



def collide(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


def update():
    for game_object in game_world.all_objects():
        game_object.update()

    for a, b, group in game_world.all_collision_pairs():
        if collide(a, b):            
            a.handle_collision(b, group)
            b.handle_collision(a, group)



def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






