from bullet import Bullet


class PlayerBullet(Bullet):
    def __init__(self, x_pos, y_pos, quadra=False):
        image = (1, 240, 0, 11, 10, 11) if not quadra else (1, 239, 11, 17, 12, 11)
        width = 11 if not quadra else 17
        height = 10 if not quadra else 12
        speed = 12
        x_pos -= width / 2
        y_pos += speed - height
        super().__init__(x_pos, y_pos, 0, -1, width, height, speed, image)
