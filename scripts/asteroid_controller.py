import random
from scripts import constant
from pygame.math import Vector2
from scripts.asteroid import Asteroid


class Asteroid_Controller(object):
    def __init__(self):
        self.asteroid_list = []

    def update_asteroids(self):
        print(len(self.asteroid_list))
        self._check_asteroid_list()
        for asteroid in self.asteroid_list:
            asteroid.update()

    def draw_asteroids(self, screen):
        for asteroid in self.asteroid_list:
            asteroid.draw(screen)


    def _get_asteroid_type(self):
        random.seed(random.randint(0,1000))
        value = random.randint(0, 1000)
        if value > 0 and value < 250:
            return 1
        elif value > 250 and value < 500:
            return 2
        elif value > 500 and value < 750:
            return 3
        elif value > 750 and value < 1000:
            return 4

    def _get_asteroid_spawn_position(self):
        random.seed(random.randint(0,1000))
        return Vector2(random.randint(0, constant.SCREEN_WIDTH), 0)

    def _spawn_asteroid(self, amount):
        for x in range(amount):
            _position = self._get_asteroid_spawn_position()
            _type = self._get_asteroid_type()

            new_asteroid = Asteroid(_position, _type)
            self.asteroid_list.append(new_asteroid)

    def _respawn_asteroid(self, asteroid):
        for x in range(asteroid.type):
            random.seed(random.randint(0,1000))
            
            _position = asteroid.position
            _type = random.randint(1, asteroid.type-1)

            new_asteroid = Asteroid(_position, _type)
            self.asteroid_list.append(new_asteroid)

    def _check_respawn(self, asteroid):
        print(asteroid.type)
        if asteroid.type == 3 or asteroid == 4:
            self._respawn_asteroid(asteroid)

    def _check_asteroid_list(self):
        if len(self.asteroid_list) == 0:
            random.seed(random.randint(0,1000))
            amount = random.randint(5, 15)
            self._spawn_asteroid(amount)

    def remove_asteroid(self, asteroid):
        if asteroid in self.asteroid_list:
            self.asteroid_list.remove(asteroid)
            self._check_respawn(asteroid)
            del asteroid