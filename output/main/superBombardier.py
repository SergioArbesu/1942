from enemy import Enemy
from player import Player
from enemyBullet import EnemyBullet
import pyxel


class SuperBombardier(Enemy):
    def __init__(self, x_pos, y_pos, player: Player):
        width = 63
        height = 48
        speed = 2
        lives = 14
        points = 2000
        image = (1, 129, 152, 63, 48, 15)
        self.travel_status = 0  # 0-4: goes up, 1-3: turns left, 2: turns right
        self.max_height = 40  # y coordinate at which it stops going up and starts turning
        self.angle = 0  # used inside the trigonometric functions when turning
        self.angle_speed = 3  # rate of change per frame of the angle
        self.turn_speed = 1  # number to which the trigonometric functions are multiplied
        self.start_frame = pyxel.frame_count
        self.frames_per_shoot = 45  # frames that pass until it shoots again
        super().__init__(x_pos, y_pos, width, height, speed, lives, points, image, player)

    def update(self):
        self.status_update()
        up = (0, 4)
        left = (1, 3)
        right = (2,)
        if self.travel_status in up:
            self.y_pos -= self.speed
        elif self.travel_status in left:
            self.angle += self.angle_speed
            self.x_pos -= pyxel.sin(self.angle) * self.turn_speed
            self.y_pos -= pyxel.cos(self.angle) * self.turn_speed
            if (pyxel.frame_count - self.start_frame) % self.frames_per_shoot == 0:
                self.shoot()
        elif self.travel_status in right:
            self.angle += self.angle_speed
            self.x_pos += pyxel.sin(self.angle) * self.turn_speed
            self.y_pos -= pyxel.cos(self.angle) * self.turn_speed
            if (pyxel.frame_count - self.start_frame) % self.frames_per_shoot == 0:
                self.shoot()
        super().update()
        self.image_update()

    # checks if it meets the requirements to change the movement pattern
    def status_update(self):
        if self.travel_status == 0 and self.y_pos <= self.max_height:
            self.travel_status = 1
        elif self.travel_status == 1 and self.angle >= 360:
            self.travel_status = 2
            self.angle = 0
        elif self.travel_status == 2 and self.angle >= 360:
            self.travel_status = 3
            self.angle = 0
        elif self.travel_status == 3 and self.angle >= 360:
            self.travel_status = 4

    # changes sprites for animation
    def image_update(self):
        if pyxel.frame_count % 2 == 0:
            x = 0
        else:
            x = 64
        self.image = (1, 129 + x, 152, 63, 48, 15)

    def shoot(self):
        # shoots 3 bullets but with no further separation than 90 degrees
        if self.is_alive and self.is_in_bounds:
            bullet_angles = [pyxel.rndi(-90, 90)]
            if bullet_angles[0] < 0:
                bullet_angles.append(bullet_angles[0] + 90 - pyxel.rndi(0, 30))
            else:
                bullet_angles.append(bullet_angles[0] - 90 + pyxel.rndi(0, 30))
            bullet_angles.append((bullet_angles[0] + bullet_angles[1]) / 2)
            for angle in bullet_angles:
                self.bullets.append(EnemyBullet(self.x_pos + self.width / 2 - 1, self.y_pos + self.height + 1,
                                                pyxel.sin(angle), pyxel.cos(angle)))
