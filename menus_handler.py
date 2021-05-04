
class MenusHandler():
    def __init__(self):
        self.menuList = [] # INCLUDES GAME
        self.current_menu = None

    def add_menu(self, menu):
        self.menuList.append(menu)

    def set_current_menu(self):
        for menu in self.menuList:
            if menu.running:
                self.current_menu = menu

    def get_current_menu(self):
        return self.current_menu

    def get_menu(self):
        self.check_for_errors()
        self.set_current_menu()
        return self.get_current_menu()

    def check_for_errors(self):
        count = 0 
        for menu in self.menuList:
            if menu.running:
                count += 1

        if count != 1:
            raise Exception('[FATAL ERROR] More then one menus are running at the same time.\nDeatils - No details cuz im lazy fuck you.')

