import pyxel


class Explosion:
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.__start = pyxel.frame_count

    @property
    def frames_passed(self):
        return pyxel.frame_count - self.__start

    @property
    def frames_per_sprite(self):
        return 2

    @property
    def frames_duration(self):
        return 6 * self.frames_per_sprite

    @property
    def image(self):
        # animation
        x = self.frames_passed // self.frames_per_sprite
        return (1, 160 + 16 * x, 200, 16, 16, 15)

    def draw(self):
        pyxel.blt(self.x_pos, self.y_pos, *self.image)
