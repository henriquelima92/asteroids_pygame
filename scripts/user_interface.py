import pygame
from scripts import constant

class Interface(object):
    def __init__(self):
        self.font = pygame.font.Font(constant.FONTS_FOLDER + 'Atari.ttf', 25) 
        self.text = self.font.render('Points: ', True, (255, 255, 255)) 
        self.textRect = self.text.get_rect()  
        self.textRect.center = (constant.SCREEN_WIDTH // 2, constant.SCREEN_HEIGHT // 2)

    def draw(self, _screen):
        _screen.blit(self.text, self.textRect)