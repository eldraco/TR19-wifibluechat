# This file is part is an addon app of the Troopers 19 Badge project, https://troopers.de/troopers19/

import display

from system import app, screen, Kernel
from machine import Pin,I2C

class StartScreen(screen.Screen):
    ACTION_ACTIVATE    = 0
    ACTION_FIND    = 1

    MENU_ITEMS = [

        {'text': 'Activate my blutooth', 'action': ACTION_ACTIVATE},
        {'text': 'Find others', 'action': ACTION_FIND},
    ]

    def on_menu_selection(self, item):
        if item['action'] == self.ACTION_ACTIVATE:
            return Kernel.ACTION_LOAD_SCREEN, 1
        elif item['action'] == self.ACTION_FIND:
            return Kernel.ACTION_LOAD_SCREEN, 2

class FindOthersScreen(screen.Screen):
    def update(self):
        self.display.fill(display.BACKGROUND)
        self.display.text('Finding Others...', 0, y=0, wrap=display.WRAP_INDENT,update=True)

    def on_text(self,event):
        if event.value is None:
            return self.back()

    def back(self, event):
        self.RENDER = True
        return Kernel.ACTION_LOAD_SCREEN, 0


class ActivateScreen(screen.Screen):

    def update(self):
        self.display.fill(display.BACKGROUND)
        self.display.text('Activating Blue Tooth', 0, y=0, wrap=display.WRAP_INDENT,update=True)

    def on_text(self,event):
        if event.value is None:
            return self.back()

        return Kernel.ACTION_RELOAD

    def back(self, event):
        self.RENDER = True
        return Kernel.ACTION_LOAD_SCREEN, 0


class App(app.App):
    VERSION = 1

    screens = [
        StartScreen(),
        ActivateScreen(),
        FindOthersScreen(),
    ]


