import pygame

pygame.init()


class Menu():
    def __init__(self, application):
        self.application = application
        self.application.menusHandler.add_menu(self)
        self.running = True

    def loop(self):
        print('menu')
        for event in self.application.events:
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    self.running = False
                    self.application.game.running = True

