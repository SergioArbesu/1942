import pyxel
from background import Background
from player import Player
from regular import Regular
from red import Red
from bombardier import Bombardier
from superBombardier import SuperBombardier
from explosion import Explosion
from powerUp import PowerUp
import time


class App:
    def __init__(self):
        pyxel.init(256, 256, title="1942")
        pyxel.load("assets/resources.pyxres")
        pyxel.load("assets/resources1.pyxres",image=False)
        pyxel.playm(1, loop=True)
        self.screen = 0  # 0: start, 1: game, 2: game_over
        self.background = Background()
        self.player = Player(100, 100)
        self.high_score = 0
        self.player_lives = 3
        self.enemies = []
        # enemy spawn periods for each enemy type
        self.enemy_spawn_time = {"regular": 4, "red": 7, "bombardier": 11, "superBombardier": 18}
        self.enemy_spawn_start = {"regular": time.time(), "red": time.time(),
                                  "bombardier": time.time(), "superBombardier": time.time()}
        self.powerups = []
        self.reds_destroyed = 0  # used to count how many reds of the same wave have been killed
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()
        if self.screen != 1:
            if pyxel.btnp(pyxel.KEY_SPACE):
                self.start()
        else:
            self.background.update()

            self.player.update()
            self.update_enemy_list()
            self.update_powerups()

            if not self.player.is_alive:
                self.player_lives -= 1
                if self.player_lives <= 0:
                    self.game_over()
                else:
                    self.restart()

            self.check_enemy_del()

    def draw(self):
        # start screen
        if self.screen == 0:
            pyxel.cls(5)
            pyxel.text(88, 110, "Press Space to start", 7)
        # game over screen
        elif self.screen == 2:
            pyxel.cls(5)
            pyxel.text(105, 70, f"Score: {self.player.score}", 7)
            pyxel.text(95, 85, f"High score: {self.high_score}", 7)
            pyxel.text(75, 100, "Press Space to play again", 7)
        # game screen
        else:
            self.background.draw()

            for powerup in self.powerups:
                powerup.draw()
            for enemy in self.enemies:
                enemy.draw()
            self.player.draw()

            pyxel.text(3, 3, f"Score: {self.player.score}", 7)
            pyxel.text(3, 11, f"Lives: {self.player_lives}", 7)

    def update_enemy_list(self):
        current_time = time.time()
        # regular enemy time pattern
        if current_time - self.enemy_spawn_start["regular"] >= self.enemy_spawn_time["regular"]:
            self.enemy_spawn_start["regular"] = current_time
            for i in range(pyxel.rndi(1, 4)):
                done = False
                while not done:
                    # checks that the regular enemy will be inside the screen when it reaches its lowest point
                    enemy = Regular(pyxel.rndi(0, pyxel.width - 1), 10 * -1 * (i + 1), self.player)
                    future_x = (enemy.travel_distance // enemy.speed) * enemy.x_speed + enemy.x_pos
                    if 0 <= future_x <= pyxel.width - enemy.width:
                        done = True
                        self.enemies.append(enemy)
        # red enemy time pattern
        if current_time - self.enemy_spawn_start["red"] >= self.enemy_spawn_time["red"]:
            self.enemy_spawn_start["red"] = current_time
            self.reds_destroyed = 5
            for x in range(0, -101, -25):  # creates the reds in a line with 25 units of interval
                self.enemies.append(Red(x, 30, self.player))
        # bombardier time pattern
        if current_time - self.enemy_spawn_start["bombardier"] >= self.enemy_spawn_time["bombardier"]:
            self.enemy_spawn_start["bombardier"] = current_time
            self.enemies.append(Bombardier(200, -40, self.player))
        # superBombardier time pattern
        if current_time - self.enemy_spawn_start["superBombardier"] >= self.enemy_spawn_time["superBombardier"]:
            self.enemy_spawn_start["superBombardier"] = current_time
            self.enemies.append(SuperBombardier(100, pyxel.height, self.player))

        # enemies list checks
        for i in range(len(self.enemies) - 1, -1, -1):
            self.enemies[i].update()

    def update_powerups(self):
        for i in range(len(self.powerups) - 1, -1, -1):
            self.powerups[i].update()
            # deletes powerup from list if it leaves the screen
            if not self.powerups[i].is_in_bounds:
                del(self.powerups[i])
            # check collision between powerup and player
            if (0 <= self.powerups[i].x_pos - self.player.x_pos <= self.player.width or
                0 <= self.powerups[i].x_pos + self.powerups[i].width - self.player.x_pos <= self.player.width) and \
               (0 <= self.powerups[i].y_pos - self.player.y_pos <= self.player.height or
                0 <= self.powerups[i].y_pos + self.powerups[i].height - self.player.y_pos <= self.player.height):
                if self.powerups[i].kind == 0:
                    self.player.quadra = True
                elif self.powerups[i].kind == 1:
                    self.player_lives += 1
                del(self.powerups[i])

    # checks if any of the enemies must be deleted (out of the screen and not bullets in its list)
    def check_enemy_del(self):
        for i in range(len(self.enemies) - 1, -1, -1):
            if type(self.enemies[i]) == Red and self.enemies[i].lives == 0:
                self.reds_destroyed -= 1
                # if all reds of a wave are destroyed, drops a power-up
                if self.reds_destroyed == 0:
                    self.powerups.append(PowerUp(self.enemies[i].x_pos, self.enemies[i].y_pos, pyxel.rndi(0, 1)))
                del(self.enemies[i])
            elif self.enemies[i].can_delete:
                del(self.enemies[i])

    # creates a new game
    def start(self):
        self.background = Background()
        self.player = Player(100, 100)
        self.player_lives = 3
        self.enemies = []
        self.powerups = []
        self.enemy_spawn_start = {"regular": time.time(), "red": time.time(),
                                  "bombardier": time.time(), "superBombardier": time.time()}
        self.screen = 1

    # restarts the enemies and powerups
    def restart(self):
        explos = Explosion(self.player.x_pos + self.player.width/2 - 8, self.player.y_pos + self.player.height/2 - 8)
        self.player = Player(100, 100, self.player.score)
        self.enemies = []
        self.powerups = []
        self.player.explosions.append(explos)

    def game_over(self):
        if self.player.score > self.high_score:
            self.high_score = self.player.score
        self.screen = 2


App()
