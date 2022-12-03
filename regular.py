from enemy import Enemy
import random
import pyxel


class Regular(Enemy):
    def __init__(self, x_pos):
        width = 5
        height = 5
        speed = 5
        fire_rate = 1
        self.x_speed = 1 * pyxel.rndf(-1, 1) # constant horizontal speed
        # distance until it starts turning
        self.travel_distance = random.randrange(int(pyxel.height / 2), pyxel.height - 20)
        self.travel_status = 0  # 0 = going down, 1 = turning, 2 = going up
        self.deceleration = 1  # positive value
        self.shot = False  # shoots this frame
        self.max_shoot_distance = 230  # maximum distance at which it will shoot when it turns
        super().__init__(x_pos, 1 - height, width, height, speed, fire_rate)

    def move(self):
        self.direction_update()
        self.x_pos += self.x_speed
        self.y_pos += self.speed

    def direction_update(self):
        if self.y_pos > self.travel_distance and self.travel_status == 0:
            self.travel_status = 1
        elif self.y_pos < self.travel_distance and self.travel_status == 1:
            self.travel_status = 2
        if self.travel_status == 1:
            # shoot if it turns
            if abs(self.speed) - self.deceleration < 0 and \
               self.y_pos + self.speed - self.deceleration < self.max_shoot_distance:
                self.shot = True
            # decelerate
            self.speed -= self.deceleration

    def shoot(self) -> bool:
        if self.shot:
            self.shot = False
            return True
        else:
            return False
