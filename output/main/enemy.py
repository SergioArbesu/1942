import pyxel
from plane import Plane
from player import Player
from explosion import Explosion


class Enemy(Plane):
    def __init__(self, x_pos, y_pos, width, height, speed, lives, points, image, player: Player):
        self.player = player
        self.lives = lives
        self.points = points
        super().__init__(x_pos, y_pos, width, height, speed, image)

    @property
    def can_delete(self) -> bool:
        return len(self.bullets) == 0 and not self.is_alive

    @property
    def is_in_bounds(self) -> bool:
        return 0 <= self.x_pos + self.width or pyxel.width >= self.x_pos or 0 <= self.y_pos + self.height or \
               pyxel.height >= self.y_pos - self.height

    @property
    def is_alive(self):
        return self.__is_alive

    @is_alive.setter
    def is_alive(self, alive):
        if self.is_in_bounds and not alive:
            self.player.explosions.append(Explosion(self.x_pos + self.width/2 - 8, self.y_pos + self.height/2 - 8))
        self.__is_alive = alive

    @property
    def lives(self):
        return self.__lives

    @lives.setter
    def lives(self, lives):
        if lives == 0:
            self.is_alive = False
            self.player.score += self.points
        self.__lives = lives

    def update(self):
        if (-200 > self.x_pos + self.width or pyxel.width + 200 < self.x_pos or -200 > self.y_pos + self.height or
                pyxel.height + 200 < self.y_pos - self.height) and self.is_alive:
            self.is_alive = False
        self.enemy_collision()
        super().update()
        self.bullet_collision()

    def enemy_collision(self):
        for i in range(len(self.player.bullets) - 1, -1, -1):
            # checks if it collides with a PlayerBullet
            if self.collision(self, self.player.bullets[i]) and self.is_alive:
                del(self.player.bullets[i])
                self.lives -= 1
                self.player.explosions.append(Explosion(self.x_pos + self.width/2 - 8, self.y_pos + self.height/2 - 8))
        # checks if it collides with the player
        if self.collision(self, self.player) and self.player.is_alive and not self.player.loop and self.is_alive:
            self.is_alive = False
            self.player.is_alive = False

    def bullet_collision(self):
        for i in range(len(self.bullets) - 1, -1, -1):
            # checks if a EnemyBullet collides with the player
            if self.collision(self.player, self.bullets[i]) and self.player.is_alive and not self.player.loop:
                del(self.bullets[i])
                self.player.is_alive = False

    # checks if two objects are touching each other
    def collision(self, objective, projectile) -> bool:
        return (0 <= projectile.x_pos - objective.x_pos <= objective.width or
                0 <= projectile.x_pos + projectile.width - objective.x_pos <= objective.width) and \
               (0 <= projectile.y_pos - objective.y_pos <= objective.height or
                0 <= projectile.y_pos + projectile.height - objective.y_pos <= objective.height)
