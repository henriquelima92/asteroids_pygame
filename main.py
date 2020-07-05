import pygame

from scripts.player import Player
from scripts.asteroid import Asteroid
from scripts.highscore import Highscore
from scripts.user_interface import Interface
from scripts.asteroid_controller import Asteroid_Controller
from scripts.audio_controller import Audio_Controller


from scripts import constant
from pygame.math import Vector2



_is_running = True

def quit_game():
    global _is_running
    _is_running = False

def _update():
    _asteroid_controller.update_asteroids()
    _player.update()

def _draw(screen):
    screen.fill([0, 0, 0])

    _asteroid_controller.draw_asteroids(screen)
    _player.draw(screen)
    _interface.draw(screen)

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

    pygame.init()
    _screen = pygame.display.set_mode([constant.SCREEN_WIDTH,constant.SCREEN_HEIGHT])
    
    _audio = Audio_Controller()
    _highscore = Highscore()
    _interface = Interface(_highscore)
    _asteroid_controller = Asteroid_Controller()
    _player = Player(_asteroid_controller, _highscore, _audio, quit_game)

    _game_loop()
    