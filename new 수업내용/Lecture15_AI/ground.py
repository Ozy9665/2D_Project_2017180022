from pico2d import *

class Ground:
    def __init__(self):
        self.image = load_image('land_before.png')

    def update(self):
        pass

    def draw(self):
        # self.image.draw(1280 // 2, 1024 // 2)
        self.image.draw(400, 30)
        self.image.draw(1200, 30)

class BackGround:
    def __init__(self):
        self.image = load_image('TheCave.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(1280 // 2, 1024 // 2)
