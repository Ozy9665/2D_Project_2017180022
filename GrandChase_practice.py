from pico2d import *

open_canvas()

grass = load_image('land_before.png')
character = load_image('Gorgos_right.png')
character2 = load_image('Gorgos_left.png')
mSlash = load_image('메가슬래쉬.png')
sFire = load_image('소드파이어.png')
cEx = load_image('크리티컬엑스.png')

x = 200

def draw_basic():             
    grass.draw(100,50)      # 지면
    grass.draw(600,50)
    mSlash.draw(50,550)    # 스킬 아이콘
    sFire.draw(120,550)
    cEx.draw(190,550)

def draw_character(character):  #캐릭터 그리기 
    character.draw(x,170)



while(True):
    while(x < 700):
        clear_canvas()
        draw_basic()
        draw_character(character)
        x = x + 2
        update_canvas()
        delay(0.01)
        get_events()
    while(x >= 100):
        clear_canvas()
        draw_basic()
        draw_character(character2)
        x = x - 2
        update_canvas()
        delay(0.01)
        get_events()

close_canvas()
