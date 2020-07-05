import pygame
from scripts import constant

class Audio_Controller(object):
    def __init__(self):
        self.ship_fire = pygame.mixer.Sound(constant.AUDIOS_FOLDER + "ship_shot.wav")
        self.ship_explosion = pygame.mixer.Sound(constant.AUDIOS_FOLDER + "ship_explosion.wav")
        self.asteroid_explosion = pygame.mixer.Sound(constant.AUDIOS_FOLDER + "asteroid_explosion.wav")

    def play_ship_shot(self):
        self.ship_fire.play()

    def play_ship_explosion(self):
        self.ship_explosion.play()

    def play_asteroid_explosion(self):
        self.asteroid_explosion.play()


