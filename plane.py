import pyxel


class Plane():
    def __init__(self, x_pos, y_pos, width, height, speed, fire_rate):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.speed = speed
        self.fire_rate = fire_rate
        self.width = width
        self.height = height
        self.image = None

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
    def fire_rate(self):
        return self.__fire_rate

    @fire_rate.setter
    def fire_rate(self, fire_rate):
        if type(fire_rate) != int and type(fire_rate) != float:
            raise TypeError("The fire_rate must be a number")
        elif fire_rate <= 0:
            raise ValueError("The fire_rate must be a positive number")
        else:
            self.__fire_rate = fire_rate

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

