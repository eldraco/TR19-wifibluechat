# TR19-wifibluechat

Version: 0.1

A Wifi and Bluetooth chat for the Troopers 19 Badge.

Before running ampy, make sure you have connection to your badge, by:

    - Connecting the USB of the badge to your computer
    - Running
        $ ampy -p /dev/tty.SLAB_USBtoUART ls
    - If you don't see a list of files
        - Move into the menu of the badge
        - Disconnect it from the PC and connect it again

## Install instructions 
    $ git clone https://github.com/eldraco/TR19-bluechat.git

    $ ampy -p /dev/tty.SLAB_USBtoUART mkdir /apps/wifibluechat
    $ ampy -p /dev/tty.SLAB_USBtoUART put TR19-wifibluechat/apps/bluechat/__init__.py /apps/wifibluechat/__init__.py
    $ ampy -p /dev/tty.SLAB_USBtoUART put TR19-wifibluechat/apps/bluechat/info.json /apps/wifibluechat/info.json
    $ ampy -p /dev/tty.SLAB_USBtoUART put TR19-wifibluechat/menu.json /menu.json

After uploading its a good idea to check that your code is there:

    $ ampy -p /dev/tty.SLAB_USBtoUART get /apps/wifibluechat/__init__.py

## Roadmap

    - Version 0.1: Only text in the app
