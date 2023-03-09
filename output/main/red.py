from enemy import Enemy
from player import Player
import pyxel


class Red(Enemy):

    def __init__(self, x_pos, y_pos, player: Player):
        width = 15
        height = 15
        speed = 5
        lives = 1
        points = 100
        image = (1, 0, 224, 14, 13, 15)
        self.left_radius_start_x = 30  # x coordinate at which it starts the first loop
        self.right_radius_start_x = 220  # x coordinate at which it starts the second loop
        self.travel_status = 0  # 0: before turns, 1: first turn, 2: between turns, 3: second turn, 4: after turns
        self.angle = 0  # used inside the trigonometric functions when turning
        self.angle_speed = 15  # rate of change per frame of the angle
        self.turn_speed = 7  # number to which the trigonometric functions are multiplied
        super().__init__(x_pos, y_pos, width, height, speed, lives, points, image, player)

    def update(self):
        self.status_update()
        move = (0, 2, 4)
        turn = (1, 3)
        if self.travel_status in move:
            self.x_pos += self.speed
        elif self.travel_status in turn:
            self.angle += self.angle_speed
            self.x_pos += pyxel.cos(self.angle) * self.turn_speed
            self.y_pos += pyxel.sin(self.angle) * self.turn_speed
        super().update()
        self.image_update()

    # checks if it meets the requirements to change the movement pattern
    def status_update(self):
        if self.travel_status == 0 and self.x_pos >= self.left_radius_start_x:
            self.travel_status = 1
        elif self.travel_status == 1 and self.angle >= 360:
            self.travel_status = 2
        elif self.travel_status == 2 and self.x_pos >= self.right_radius_start_x:
            self.travel_status = 3
            self.angle = 0
        elif self.travel_status == 3 and self.angle >= 360:
            self.travel_status = 4

    # changes sprites for animation
    def image_update(self):
        y = 0
        if pyxel.frame_count % 2 == 0:
            y = 16
        x = (self.angle + 11.25) // 22.5
        if x == 16:
            x = 0
        self.image = (1, x * 16, 224 + y, 15, 15, 15)
