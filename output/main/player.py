import pyxel
from plane import Plane
from explosion import Explosion
from playerBullet import PlayerBullet


class Player(Plane):
    def __init__(self, x_pos, y_pos, score=0):
        width = 25
        height = 16
        speed = 4
        image = (1, 0, 0, 25, 16, 8)
        self.explosions: list[Explosion] = []
        self.quadra = False
        self.score = score
        self.loop = False
        self.start_loop = 0
        self.original = (0, 0)
        super().__init__(x_pos, y_pos, width, height, speed, image)

    @property
    def is_alive(self):
        return self.__is_alive

    @is_alive.setter
    def is_alive(self, alive):
        if not alive:
            self.explosions.append(Explosion(self.x_pos + self.width / 2 - 8, self.y_pos + self.height / 2 - 8))
        self.__is_alive = alive

    def update(self):
        if pyxel.btnp(pyxel.KEY_Z) and not self.loop:
            self.loop = True
            self.start_loop = pyxel.frame_count
            self.original = (self.x_pos, self.y_pos)

        if self.loop:
            self.loop_update()
        else:
            self.image_update()

            # player movement input
            x_dir, y_dir = 0, 0
            if pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_RIGHT):
                x_dir = 1
            if pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.KEY_LEFT):
                x_dir = -1
            if pyxel.btn(pyxel.KEY_W) or pyxel.btn(pyxel.KEY_UP):
                y_dir = -1
            if pyxel.btn(pyxel.KEY_S) or pyxel.btn(pyxel.KEY_DOWN):
                y_dir = 1
            self.x_pos += self.speed * x_dir / pyxel.sqrt(x_dir**2 + y_dir**2)
            self.y_pos += self.speed * y_dir / pyxel.sqrt(x_dir**2 + y_dir**2)
            # vectores unitarios para mantener la velocidad constante independientemente de la dirección

            if 0 > self.x_pos:
                self.x_pos = 0
            elif pyxel.width < self.x_pos + self.width:
                self.x_pos = pyxel.width - self.width
            if 0 > self.y_pos:
                self.y_pos = 0
            elif pyxel.height < self.y_pos + self.height:
                self.y_pos = pyxel.height - self.height

            if pyxel.btnp(pyxel.KEY_SPACE):
                self.shoot()

        super().update()
        self.explosion_update()

    def image_update(self):
        # player image animation
        if pyxel.frame_count % 2 == 0:
            self.image = (1, 0, 0, 25, 16, 8)
        else:
            self.image = (1, 25, 0, 25, 16, 8)

    def explosion_update(self):
        for i in range(len(self.explosions) - 1, -1, -1):
            if self.explosions[i].frames_passed >= self.explosions[i].frames_duration:
                del(self.explosions[i])

    def draw(self):
        for i in range(len(self.explosions)):
            self.explosions[i].draw()
        super().draw()

    def shoot(self):
        if self.is_alive:
            bullet = PlayerBullet(self.x_pos + self.width / 2, self.y_pos + 1, self.quadra)
            self.bullets.append(bullet)

    def loop_update(self):
        animation = ((1, 50, 0, 28, 14, 15), (1, 50, 14, 27, 12, 15), (1, 78, 0, 29, 10, 15),
                     (1, 78, 10, 27, 7, 15), (1, 107, 0, 27, 13, 15), (1, 134, 0, 30, 17, 15),
                     (1, 164, 0, 32, 22, 15), (1, 196, 0, 32, 25, 15), (1, 0, 152, 30, 21, 15),
                     (1, 30, 152, 28, 17, 15), (1, 58, 152, 27, 12, 15), (1, 58, 165, 25, 7, 15),
                     (1, 85, 152, 25, 8, 15), (1, 0, 173, 25, 11, 15), (1, 85, 160, 25, 13, 15))
        index = (pyxel.frame_count - self.start_loop) // 3
        self.image = animation[index]
        self.x_pos = self.original[0] + self.width / 2 - animation[index][3] / 2
        self.y_pos = self.original[1] + self.height / 2 - animation[index][4] / 2
        if index == 14:
            self.loop = False
            self.x_pos = self.original[0]
            self.y_pos = self.original[1]
