import pygame

pygame.init()


class Game():
    def __init__(self, application):
        self.application = application
        self.application.menusHandler.add_menu(self)
        self.running = False

    def loop(self):
        print('game')
        for event in self.application.events:
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    self.running = False
                    self.application.menu.running = True

