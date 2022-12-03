import pyxel
from plane import Plane
import time


class Enemy(Plane):
    def __init__(self, x_pos, y_pos, width, height, speed, fire_rate):
        super().__init__(x_pos, y_pos, width, height, speed, fire_rate)
        self.start = time.time()

    def shoot(self):
        pass
