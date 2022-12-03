import pyxel
from plane import Plane


class Player(Plane):
    #  width y height de Player son constantes asi que las crearemos aqui cuando sepamos los valores

    def __init__(self, x_pos, y_pos):
        width = 10
        height = 10
        speed = 4
        fire_rate = 20
        super().__init__(x_pos, y_pos, width, height, speed, fire_rate)

    def move(self, x_dir, y_dir):
        self.x_pos += self.speed * x_dir / pyxel.sqrt(x_dir**2 + y_dir**2)
        self.y_pos += self.speed * y_dir / pyxel.sqrt(x_dir**2 + y_dir**2)
        # vectores unitarios para mantener la velocidad independientemente de la dirección

        if 0 > self.x_pos:
            self.x_pos = 0
        elif pyxel.width < self.x_pos + self.width:
            self.x_pos = pyxel.width - self.width
        if 0 > self.y_pos:
            self.y_pos = 0
        elif pyxel.height < self.y_pos + self.height:
            self.y_pos = pyxel.height - self.height

    def z_flip(self):
        pass
