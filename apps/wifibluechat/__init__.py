# This file is part is an addon app of the Troopers 19 Badge project, https://troopers.de/troopers19/

import display
import network
import system
import socket
import time

from system import app, screen, Kernel
from machine import Pin,I2C

class StartScreen(screen.Screen):
    ACTION_ACTIVATE    = 0
    ACTION_FIND    = 1

    MENU_ITEMS = [

        {'text': 'Activate my server...', 'action': ACTION_ACTIVATE},
        {'text': 'Find others...', 'action': ACTION_FIND},
    ]

    def on_menu_selection(self, item):
        if item['action'] == self.ACTION_ACTIVATE:
            return Kernel.ACTION_LOAD_SCREEN, 1
        elif item['action'] == self.ACTION_FIND:
            return Kernel.ACTION_LOAD_SCREEN, 2

class FindOthersScreen(screen.Screen):
    """
    self.text
    """

    def update(self):
        self.display.fill(display.BACKGROUND)
        self.display.text('Finding the top 5 badges around you...', 0, y=0, wrap=display.WRAP_INDENT,update=True)
        self.input.get_user_input(self,1,title='Send:',title_wrap=display.WRAP_INDENT)
        self.display.text(self.response, 1, y=0, wrap=display.WRAP_INDENT,update=True)

        # Create the nic object
        nic = network.WLAN(network.STA_IF)
        nic.active(True)
        aps = nic.scan()
        #for i in range(len(aps)):
        for i in range(0,5):
            text = str(aps[i][0].decode('utf-8'))
            pos = 10* (i + 1)
            self.display.text(text, 0, y=pos, wrap=display.WRAP_INDENT,update=True)
        # connect
        self.display.text('Connecting to your pear...', 0, y=60, wrap=display.WRAP_INDENT,update=True)
        nic.connect('latinos-badge', 'chingatumadre')

        if not nic.isconnected():
            return Kernel.ACTION_LOAD_SCREEN, 0
        self.display.fill(display.BACKGROUND)
        ip = str(nic.ifconfig())
        self.display.text('Connected to WiFi! We have IP {}'.format(ip), 0, y=00, wrap=display.WRAP_INDENT,update=True)
        time.sleep(1)
        
        # Send text
        self.display.fill(display.BACKGROUND)
	s = socket.socket()
        host = '192.168.4.1'
	addr = socket.getaddrinfo(host, 80)[0][-1]
	s.connect(addr)
        self.display.text('Connected to server...', 0, y=0, wrap=display.WRAP_INDENT,update=True)


        pos = 20
        while True:
            # Send chat
            self.display.text('Sending...', 0, y=pos, wrap=display.WRAP_INDENT,update=True)
            s.send(bytes('hola de sebas', 'utf8'))
            #s.send(data)
            self.display.text('Receiving...', 0, y=pos+10, wrap=display.WRAP_INDENT,update=True)
            data = s.recv(100)
            self.display.text(str(data), 0, y=pos+20, wrap=display.WRAP_INDENT,update=True)
            pos += 30

        return Kernel.ACTION_LOAD_SCREEN, 0


    def on_text(self,event):
        if event.value is None:
            return self.back()
        self.response = ''
        value = event.value.lower()
        if value == "":
            return Kernel.ACTION_RELOAD
        self.response = value
        return Kernel.ACTION_RELOAD

    def back(self, event):
        self.RENDER = True
        return Kernel.ACTION_LOAD_SCREEN, 0


class ActivateScreen(screen.Screen):

   def update(self):
        self.display.fill(display.BACKGROUND)
        self.display.text('Activating WiFi Server...', 0, y=0, wrap=display.WRAP_INDENT,update=True)

        # Create the nic object
        nic = network.WLAN(network.AP_IF)
        nic2 = network.WLAN(network.STA_IF)
        if nic.isconnected():
            nic.disconnect()
        if nic2.isconnected():
            nic2.disconnect()
        if nic.active():
            nic.active(False)
        if nic2.active():
            nic2.active(False)

        nic.active(True)
        nic.config(essid="latinos-badge", password="chingatumadre", authmode=3)
        
        time.sleep(1)
        if nic.active():
            self.display.fill(display.BACKGROUND)
            self.display.text('Running!', 0, y=0, wrap=display.WRAP_INDENT,update=True)
            ip = nic.ifconfig()[0]
            self.display.text(str(ip), 0, y=10, wrap=display.WRAP_INDENT,update=True)

            addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
            s = socket.socket()
            s.bind(addr)
            s.listen(1)
            msg = "Hola desde Mexico"
            while True:
                cl, addr = s.accept()
                cl.send(msg)
                data = cl.recv(100)
                if data:
                    print(str(data, 'utf8'), end='')
                else:
                    break
                s.close()
        else:
            self.display.fill(display.BACKGROUND)
            self.display.text('Not Running... :-(', 0, y=0, wrap=display.WRAP_INDENT,update=True)
        
        return self.back()

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


