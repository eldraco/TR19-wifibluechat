# TR19-bluechat

A Bluetooth chat for the Troopers 19 Badge.

Before running ampy, make sure you have connection to your badge, by:
    - Connecting the USB of the badge to your computer
    - Running
        $ ampy -p /dev/tty.SLAB_USBtoUART ls
    - If you don't see a list of files
        - Move into the menu of the badge
        - Disconnect it from the PC and connect it again

## Install instructions 
    $ git clone https://github.com/eldraco/TR19-bluechat.git

    $ cd TR19-bluechat
    $ ampy -p /dev/tty.SLAB_USBtoUART mkdir /apps/bluechat
    $ ampy -p /dev/tty.SLAB_USBtoUART put TR19-bluechat/apps/bluechat/__init__.py /apps/bluechat/__init__.py
    $ ampy -p /dev/tty.SLAB_USBtoUART put TR19-bluechat/apps/bluechat/info.json /apps/bluechat/info.json
    $ ampy -p /dev/tty.SLAB_USBtoUART put TR19-bluechat/menu.json /menu.json
