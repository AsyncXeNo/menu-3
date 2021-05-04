import pygame
import sys

from constants import *
from menus_handler import MenusHandler
from game import Game
from menu import Menu

class Application():
    def __init__(self):

        pygame.init()

        self._width = WIDTH
        self._height = HEIGHT 
        self._caption = CAPTION

        self.win = pygame.display.set_mode((self._width, self._height))
        pygame.display.set_caption(self._caption)

        self._clock = pygame.time.Clock()
        self._fps = FPS

        self.running = True
        self.events = []

        self.menusHandler = MenusHandler()

        # Always define these at the end

        self.game = Game(self)
        self.menu = Menu(self)

        self._run()

    def _update_events(self):
        self.events = pygame.event.get()

    def _events_handler(self):
        for event in self.events:
            if event.type == pygame.QUIT:
                print('APPPLICATION CLOSED')
                self.running = False
                pygame.quit()
                sys.exit()

    def _run(self):
        while self.running:
            self._clock.tick(self._fps)
            self.win.fill(pygame.Color('black'))

            self._update_events()

            self.menusHandler.get_menu().loop()

            self._events_handler()

            pygame.display.update()
