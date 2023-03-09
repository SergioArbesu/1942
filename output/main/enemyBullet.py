from bullet import Bullet


class EnemyBullet(Bullet):
    def __init__(self, x_pos, y_pos, x_dir, y_dir):
        width = 4
        height = 4
        speed = 3
        image = (1, 252, 0, 4, 4, 11)
        super().__init__(x_pos, y_pos, x_dir, y_dir, width, height, speed, image)
