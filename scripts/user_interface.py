import pygame
from scripts import constant

class Interface(object):
    def __init__(self, highscore):
        self.highscore = highscore
        self.font = pygame.font.Font(constant.FONTS_FOLDER + 'Atari.ttf', 25) 
        self.text = self.font.render('Points: ' + str(self.highscore.current_points), True, (255, 255, 255))
        self.textRect = self.text.get_rect()  
        self.textRect.center = (70, 20)

    def draw(self, _screen):
        self.text = self.font.render('Points: ' + str(self.highscore.current_points), True, (255, 255, 255))
        _screen.blit(self.text, self.textRect)