from enemy import Enemy


class SuperBombardier(Enemy):
    def __init__(self, x_pos, y_pos):
        width = 10
        height = 10
        speed = 1
        fire_rate = 1
        super().__init__(x_pos, y_pos, width, height, speed, fire_rate)

    def move(self):
        pass
