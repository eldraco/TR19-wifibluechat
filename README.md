# TR19-bluechat

## Install instructions 
    $ git clone https://github.com/eldraco/TR19-bluechat.git

    $ cd TR19-bluechat
    $ ampy -p /dev/tty.SLAB_USBtoUART mkdir /apps/bluechat
    $ ampy -p /dev/tty.SLAB_USBtoUART put TR19-bluechat/apps/bluechat/__init__.py /apps/bluechat/__init__.py
    $ ampy -p /dev/tty.SLAB_USBtoUART put TR19-bluechat/apps/bluechat/info.json /apps/bluechat/info.json
    $ ampy -p /dev/tty.SLAB_USBtoUART put TR19-bluechat/menu.json /menu.json
