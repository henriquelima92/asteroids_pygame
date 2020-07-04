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

    def asteroid_creator(self):
        random.seed(random.randint(0,100))
        random_value = random.randint(0,100)

        if random_value > 0 and random_value < 25: #type 1
            return Vector2(10,10)
        elif random_value >= 25 and random_value < 50: #type 2
            return Vector2(20,20)
        elif random_value >= 50 and random_value < 75: #type 3
            return Vector2(30,30)
        else: #type 4
            return Vector2(40,40)

    def spawn(self):
        asteroids_length = random.randint(5, 10)
        for index in range(0, asteroids_length):
            random.seed(random.randint(0,100))
            position = Vector2(random.randint(10, 590), 10)
            asteroid_type = self.asteroid_creator()

            asteroid = Asteroid(position, asteroid_type)
            self.asteroid_list.append(asteroid)
    
    def check_asteroid_list(self):
        if len(self.asteroid_list) == 0:
            self.spawn()