import pyxel
from bullet import Bullet


class Plane:
    def __init__(self, x_pos, y_pos, width, height, speed, image):
        self.x_pos = x_pos  # position in the x-axis
        self.y_pos = y_pos  # position in the y-axis
        self.speed = speed  # rate of change of the position
        self.width = width  # width it is considered to have
        self.height = height  # height it is considered to have
        self.image = image  # a 6 element tuple that represents the last 6 arguments of the pyxel.blt() method
        self.bullets = []  # bullets shot by the object
        self.is_alive = True  # whether the object is still alive or not

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
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        if type(speed) != int and type(speed) != float:
            raise TypeError("Speed must be a number")
        else:
            self.__speed = speed

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) != int and type(width) != float:
            raise TypeError("The width must be a number")
        elif width <= 0:
            raise ValueError("The width must be a positive number")
        else:
            self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) != int and type(height) != float:
            raise TypeError("The height must be a number")
        elif height <= 0:
            raise ValueError("The height must be a positive number")
        else:
            self.__height = height

    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, image: tuple[int, int, int, int, int, int]):
        if type(image) != tuple:
            raise TypeError("the image must be a tuple")
        elif len(image) != 6:
            raise ValueError("the image must have 6 elements")
        else:
            self.__image = image

    @property
    def bullets(self):
        return self.__bullets

    @bullets.setter
    def bullets(self, bullets):
        if type(bullets) != list:
            raise TypeError("bullets must be a list")
        else:
            self.__bullets = bullets

    def update(self):
        self.bullet_update()

    def bullet_update(self):
        for i in range(len(self.bullets) - 1, -1, -1):
            self.bullets[i].update()
            if not self.bullets[i].is_in_bounds:
                del(self.bullets[i])

    def draw(self):
        if self.is_alive:
            pyxel.blt(self.x_pos, self.y_pos, *self.image)
        for i in range(len(self.bullets)):
            self.bullets[i].draw()
