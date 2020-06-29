import pygame
from scripts.player import Player
from scripts.asteroid import Asteroid
from scripts import constant
from pygame.math import Vector2
from scripts.asteroid_controller import Asteroid_Controller

_is_running = True


def _update():
    _asteroid_controller.update()
    _player.update(_asteroid_controller)

def _draw(screen):
    screen.fill([0, 0, 0])
    
    _asteroid_controller.draw(screen)
    _player.draw(screen)

    font = pygame.font.Font('Atari.ttf', 25) 
    text = font.render('Points: ', True, white) 

    textRect = text.get_rect()  
    textRect.center = (constant.SCREEN_WIDTH // 2, constant.SCREEN_HEIGHT // 2) 

    _screen.blit(text, textRect)

    pygame.display.update()

def _inputs():
    global _is_running
    
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                _is_running = False
            _player.inputs(event)

def _game_loop():

    while _is_running == True: 
        _inputs()
        _update()
        _draw(_screen)

    pygame.quit()


if __name__ == '__main__':
    global _screen

    black = (0, 0, 0) 
    blue = (0, 0, 128)
    white = (255, 255, 255)

    pygame.init()
    _screen = pygame.display.set_mode([constant.SCREEN_WIDTH,constant.SCREEN_HEIGHT])


    _asteroid_controller = Asteroid_Controller()
    _player = Player()


    _game_loop()
    