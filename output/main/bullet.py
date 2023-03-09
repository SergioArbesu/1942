import pyxel


class Bullet:
    def __init__(self, x_pos, y_pos, x_dir, y_dir, width, height, speed, image):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.speed = speed
        self.x_dir = x_dir
        self.y_dir = y_dir
        self.image = image

    @property
    def x_pos(self):
        return self.__x_pos

    @x_pos.setter
    def x_pos(self, x_pos):
        if type(x_pos) != int and type(x_pos) != float:
            raise TypeError("The x_pos must be a number")
        else:
            self.__x_pos = x_pos

    @property
    def y_pos(self):
        return self.__y_pos

    @y_pos.setter
    def y_pos(self, y_pos):
        if type(y_pos) != int and type(y_pos) != float:
            raise TypeError("The y_pos must be a number")
        else:
            self.__y_pos = y_pos

    @property
    def x_dir(self):
        return self.__x_dir

    @x_dir.setter
    def x_dir(self, x_dir):
        if type(x_dir) != int and type(x_dir) != float:
            raise TypeError("the x_dir must be a number")
        else:
            self.__x_dir = x_dir

    @property
    def y_dir(self):
        return self.__y_dir

    @y_dir.setter
    def y_dir(self, y_dir):
        if type(y_dir) != int and type(y_dir) != float:
            raise TypeError("the y_dir must be a number")
        else:
            self.__y_dir = y_dir

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        if type(speed) != int and type(speed) != float:
            raise TypeError("Speed must be a number")
        else:
            self.__speed = speed

    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, image):
        if type(image) != tuple:
            raise TypeError("the image must be a tuple")
        elif len(image) != 6:
            raise ValueError("the image must have 6 elements")
        else:
            self.__image = image

    @property
    def is_in_bounds(self):
        return 0 <= self.x_pos + self.width and pyxel.width >= self.x_pos and 0 <= self.y_pos + self.height and \
               pyxel.height >= self.y_pos - self.height

    def update(self):
        self.x_pos += self.speed * self.x_dir / pyxel.sqrt(self.x_dir**2 + self.y_dir**2)
        self.y_pos += self.speed * self.y_dir / pyxel.sqrt(self.x_dir**2 + self.y_dir**2)
        # vectores unitarios para mantener la velocidad independientemente de la dirección

    def draw(self):
        pyxel.blt(self.x_pos, self.y_pos, *self.image)
