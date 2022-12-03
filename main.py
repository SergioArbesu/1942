import pyxel
from player import Player
from regular import Regular
from red import Red
from bombardier import Bombardier
from superBombardier import SuperBombardier
from bullet import Bullet
import time
import random


class App:
    def __init__(self):
        pyxel.init(450, 601)
        self.player = Player(10, 10)
        self.score = 0
        self.high_score = 0
        self.lives = 3
        self.enemies = []
        self.regular_spawn_time = 4
        self.regular_spawn_start = time.time()
        self.bullets = []
        pyxel.run(self.update, self.draw)

    def update(self):
        self.update_bullet_list()
        self.update_enemy_list()

        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()
        # player movement input
        x, y = 0, 0
        if pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_RIGHT):
            x = 1
        if pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.KEY_LEFT):
            x = -1
        if pyxel.btn(pyxel.KEY_W) or pyxel.btn(pyxel.KEY_UP):
            y = -1
        if pyxel.btn(pyxel.KEY_S) or pyxel.btn(pyxel.KEY_DOWN):
            y = 1
        self.player.move(x, y)

        # player shoot input
        if pyxel.btnp(pyxel.KEY_SPACE):
            bullet = Bullet(self.player.x_pos + self.player.width / 2, self.player.y_pos - 1, 0, -1, 3)
            self.bullets.append(bullet)

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.player.x_pos, self.player.y_pos, 10, 10, 2)
        self.draw_bullet_list()
        self.draw_enemy_list()

        # pyxel.cls(4)
        # pyxel.rect(self.red.x_pos, self.red.y_pos, 10, 10, 2)
        # for i in range(len(self.bullets)):
        #     pyxel.rect(self.bullets[i].x_pos, self.bullets[i].y_pos, 1, 1, 7)

    def update_bullet_list(self):
        for i in range(len(self.bullets) - 1, -1, -1):
            self.bullets[i].move()
            # deletes the bullet if it is out of bounds
            if not 0 < self.bullets[i].x_pos < pyxel.width and not 0 < self.bullets[i].y_pos < pyxel.height:
                del(self.bullets[i])

    def update_enemy_list(self):
        if time.time() - self.regular_spawn_start >= self.regular_spawn_time:
            self.regular_spawn_start = time.time()
            for _ in range(random.randint(1,4)):
                self.enemies.append(Regular(random.randrange(pyxel.width)))

        # enemy movement
        for i in range(len(self.enemies) - 1, -1, -1):
            # create a bullet if shoot returns True
            if self.enemies[i].shoot():
                self.bullets.append(Bullet(self.enemies[i].x_pos + self.enemies[i].width / 2,
                                           self.enemies[i].y_pos + 1, self.player.x_pos - self.enemies[i].x_pos,
                                           self.player.y_pos - self.enemies[i].y_pos, 3))
            self.enemies[i].move()
            # delete if it is completely out of bounds
            if (0 > self.enemies[i].x_pos + self.enemies[i].width or pyxel.width < self.enemies[i].x_pos -
                self.enemies[i].width) and (0 > self.enemies[i].y_pos + self.enemies[i].height or pyxel.height <
                                            self.enemies[i].y_pos - self.enemies[i].height):
                del(self.enemies[i])

    def draw_bullet_list(self):
        for i in range(len(self.bullets)):
            pyxel.rect(self.bullets[i].x_pos, self.bullets[i].y_pos, 1, 1, 7)

    def draw_enemy_list(self):
        for enemy in self.enemies:
            pyxel.rect(enemy.x_pos, enemy.y_pos, enemy.width, enemy.height, 9)

    def music(self):
        pass


App()
