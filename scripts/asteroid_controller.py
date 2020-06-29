import random
from pygame.math import Vector2
from scripts.asteroid import Asteroid


class Asteroid_Controller(object):
    def __init__(self):
        self.asteroid_list = []

    def update(self):
        self.check_asteroid_list()
        for asteroid in self.asteroid_list:
            asteroid.update()

    def draw(self, screen):
        for asteroid in self.asteroid_list:
            asteroid.draw(screen)

    def spawn(self):
        asteroids_length = random.randint(5, 10)
        for index in range(0, asteroids_length):
            random.seed(random.randint(0,100))
            position = Vector2(random.randint(10, 590), 10)
            asteroid = Asteroid(position)
            self.asteroid_list.append(asteroid)
    
    def check_asteroid_list(self):
        if len(self.asteroid_list) == 0:
            self.spawn()