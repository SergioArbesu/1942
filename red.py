from enemy import Enemy


class Red(Enemy):
    def __init__(self, x_pos, y_pos):
        width = 5
        height = 5
        speed = 1
        fire_rate = 1
        super().__init__(x_pos, y_pos, width, height, speed, fire_rate)

    def move(self):
        #self.direction_update()
        #self.x_pos += self.x_speed
        #self.y_pos += self.speed
        pass

    # if self.y_pos > self.travel_distance:
    #   self.speed *= -1
