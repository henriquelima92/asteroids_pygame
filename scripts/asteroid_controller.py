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

    def asteroid_creator(self, respaw):
        # random.seed(random.randint(0,100))
        random_value = random.randint(0,100) if respaw == False else random.randint(0,50)

        if random_value > 0 and random_value < 25: #type 1
            return Vector2(10,10), 1
        elif random_value >= 25 and random_value < 50: #type 2
            return Vector2(20,20), 2
        elif random_value >= 50 and random_value < 75: #type 3
            return Vector2(30,30), 3
        else: #type 4
            return Vector2(40,40), 4

    def asteroid_remover(self, asteroid):
        self.asteroid_list.remove(asteroid)
        asteroid.kill()

        self.spawn_when_kill(random.randint(1, 4), asteroid)  

    def spawn_when_kill(self, asteroids_length, asteroid):
        if asteroid.asteroid_type == 3 or asteroid.asteroid_type == 4:
            for ast in range(0, asteroids_length):
                position = asteroid.position
                scale, asteroid_type = self.asteroid_creator(True)
                print(scale)
                print(asteroid_type)
                new_asteroid = Asteroid(position, scale, asteroid_type)
                self.asteroid_list.append(new_asteroid)


    def spawn(self, asteroids_length, asteroids_position):
        for index in range(0, asteroids_length):
            random.seed(random.randint(0,100))
            position = None

            if asteroids_position == None:
                position = Vector2(random.randint(10, 590), 10)
            else:
                position = asteroids_position

            scale, asteroid_type = self.asteroid_creator(False)
            asteroid = Asteroid(position, scale, asteroid_type)
            self.asteroid_list.append(asteroid)
    
    def check_asteroid_list(self):
        if len(self.asteroid_list) == 0:
            self.spawn(random.randint(5, 10), None)