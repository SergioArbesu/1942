from enemy import Enemy
from player import Player
from enemyBullet import EnemyBullet
import pyxel


class Bombardier(Enemy):
    def __init__(self, x_pos, y_pos, player: Player):
        width = 31
        height = 23
        speed = 2.5
        lives = 6
        points = 1000
        image = (1, 0, 72, 31, 23, 15)
        self.travel_status = 0  # 0-6: goes up, 1-3-5: turns clockwise, 2: goes left, 4: goes right
        self.max_height = 100  # y coordinate at which the plane will start to turn
        self.max_x = pyxel.width - x_pos  # x coordinate at which the plane will start to turn
        self.angle = 0  # used inside the trigonometric functions when turning
        self.angle_speed = 5  # rate of change per frame of the angle
        self.turn_speed = 2  # number to which the trigonometric functions are multiplied
        super().__init__(x_pos, y_pos, width, height, speed, lives, points, image, player)

    def update(self):
        self.status_update()
        down = (0, 6)
        turn = (1, 3, 5)
        if self.travel_status in down:
            self.y_pos += self.speed
        elif self.travel_status in turn:
            self.angle += self.angle_speed
            self.x_pos -= pyxel.sin(self.angle) * self.turn_speed
            self.y_pos += pyxel.cos(self.angle) * self.turn_speed
        elif self.travel_status == 2:
            self.x_pos -= self.speed
        elif self.travel_status == 4:
            self.x_pos += self.speed
        super().update()
        self.image_update()

    # checks if it meets the requirements to change the movement pattern
    def status_update(self):
        if self.travel_status == 0 and self.y_pos >= self.max_height:
            self.travel_status = 1
            self.shoot()
        elif self.travel_status == 1 and self.angle >= 90:
            self.travel_status = 2
            self.x_angle = self.x_pos
        elif self.travel_status == 2 and self.x_pos <= self.max_x:
            self.travel_status = 3
        elif self.travel_status == 3 and self.angle >= 270:
            self.travel_status = 4
        elif self.travel_status == 4 and self.x_pos >= self.x_angle:
            self.travel_status = 5
        elif self.travel_status == 5 and self.angle >= 360:
            self.travel_status = 6

    # changes sprites for animation
    def image_update(self):
        y = 0
        if pyxel.frame_count % 2 == 0:
            y = 56
        var = (self.angle + 11.25) // 22.5
        if var == 1:
            self.image = (1, 228, 41 + y, 26, 23, 15)
        elif var == 2:
            self.image = (1, 194, 42 + y, 26, 23, 15)
        elif var == 3:
            self.image = (1, 164, 42 + y, 26, 22, 15)
        elif var == 4:
            self.image = (1, 134, 39 + y, 25, 25, 15)
        elif var == 5:
            self.image = (1, 106, 39 + y, 23, 23, 15)
        elif var == 6:
            self.image = (1, 68, 40 + y, 26, 24, 15)
        elif var == 7:
            self.image = (1, 35, 40 + y, 29, 23, 15)
        elif var == 8:
            self.image = (1, 0, 40 + y, 31, 23, 15)
        elif var == 9:
            self.image = (1, 224, 73 + y, 31, 23, 15)
        elif var == 10:
            self.image = (1, 196, 72 + y, 28, 24, 15)
        elif var == 11:
            self.image = (1, 165, 71 + y, 27, 24, 15)
        elif var == 12:
            self.image = (1, 135, 65 + y, 25, 27, 15)
        elif var == 13:
            self.image = (1, 105, 65 + y, 24, 23, 15)
        elif var == 14:
            self.image = (1, 71, 72 + y, 27, 23, 15)
        elif var == 15:
            self.image = (1, 38, 72 + y, 29, 23, 15)
        else:
            self.image = (1, 0, 72 + y, 31, 23, 15)

    def shoot(self):
        if self.is_alive and self.is_in_bounds:
            # shoots towards the player
            bullet = EnemyBullet(self.x_pos + self.width / 2 - 1, self.y_pos + self.height + 1,
                                 self.player.x_pos + self.player.width / 2 - (self.x_pos + self.width / 2),
                                 self.player.y_pos + self.player.height / 2 - (self.y_pos + self.height + 1))
            self.bullets.append(bullet)
