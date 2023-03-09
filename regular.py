from enemy import Enemy
from player import Player
from enemyBullet import EnemyBullet
import random
import pyxel


class Regular(Enemy):

    def __init__(self, x_pos, y_pos, player: Player):
        width = 15
        height = 14
        speed = 5
        lives = 1
        points = 50
        image = (1, 0, 200, 15, 14, 15)
        self.x_speed = 1.5 * pyxel.rndf(-1, 1)  # constant horizontal speed
        self.travel_distance = pyxel.rndf(player.y_pos - 60, player.y_pos)  # y coordinate at which it starts turning
        self.travel_status = 0  # 0: goes down, 1: turns, 2: goes up
        self.turn_start = 0  # frame count at which it starts turning
        self.turn_frames = 3  # frames per sprite of the animation
        super().__init__(x_pos, y_pos, width, height, speed, lives, points, image, player)

    def update(self):
        self.direction_update()

        self.x_pos += self.x_speed
        if self.travel_status != 1:
            self.y_pos += self.speed
        super().update()
        self.image_update()

    # checks if it meets the requirements to change the movement pattern
    def direction_update(self):
        if self.y_pos > self.travel_distance and self.travel_status == 0:
            self.travel_status = 1
            self.turn_start = pyxel.frame_count
            self.shoot()
        elif self.travel_status == 1 and pyxel.frame_count - self.turn_start >= self.turn_frames * 3:
            self.travel_status = 2
            self.speed *= -1

    # changes sprites for animation
    def image_update(self):
        if self.travel_status == 0:
            if pyxel.frame_count % 2 == 0:
                self.image = (1, 0, 192, 15, 14, 15)
            else:
                self.image = (1, 16, 192, 15, 14, 15)
        elif self.travel_status == 2:
            if pyxel.frame_count % 2 == 0:
                self.image = (1, 32, 192, 15, 14, 15)
            else:
                self.image = (1, 48, 192, 15, 14, 15)
        else:
            var = (pyxel.frame_count - self.turn_start) // self.turn_frames
            self.image = (1, var * 16, 208, 15, 14, 15)

    def shoot(self):
        # only shoots 1 every 4 times
        rndm = pyxel.rndi(1, 4)
        if self.is_alive and self.is_in_bounds and rndm == 4 and self.y_pos + self.height < self.player.y_pos:
            # shoots towards the player
            bullet = EnemyBullet(self.x_pos + self.width / 2 - 1, self.y_pos + self.height + 1,
                                 self.player.x_pos + self.player.width / 2 - (self.x_pos + self.width / 2),
                                 self.player.y_pos + self.player.height / 2 - (self.y_pos + self.height + 1))
            self.bullets.append(bullet)
