import pyxel
# TODO: hacer que aparezcan los powerups


class PowerUp:
    def __init__(self, x_pos, y_pos, kind):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = 13
        self.height = 10
        self.speed = 1
        self.kind = kind  # 0: quadra, 1: live

    @property
    def image(self):
        return (1, 49 + self.kind * 16, 210, 13, 10, 15)

    @property
    def is_in_bounds(self):
        return 0 <= self.y_pos + self.height or pyxel.height >= self.y_pos - self.height

    def update(self):
        self.y_pos += self.speed

    def draw(self):
        pyxel.blt(self.x_pos, self.y_pos, *self.image)
