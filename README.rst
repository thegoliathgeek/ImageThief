IMAGE THIEF
===============

This is a python library for capturing images over default route (http://0.0.0.0)

Functions:
----------
* Capture images from raspberryPi and access on your system.
* Capture images on one system and access on other.

Note:
~~~~~
::

   Don't forget to install opencv (Not included in this packages)

Installation :
--------------

Python3
-------

::

    python3 -m pip install imagethief --user


Server Demo:
~~~~~~~~~~~~

::

    from ImageThief import Thief


    def some():
        print('Image stolen')
        pass

    if __name__ == '__main__':
        thief = Thief('Name', cameraPort=0)
        thief.add_plan('/image', 'image', some)
        thief.steal(port=5000, debug=True)


Client Demo:
~~~~~~~~~~~~
::

   import requests as req
   from ImageThief import StolenImageDecoder

   if __name__ == '__main__':
        your_ip = '<your server ip>'
        port = 5000 #default
        url = 'http://'+your_ip+':'+str(port)+'/plan_name'
        # For above Demo code it is
        # url = 'http://'+your_ip+':'+str(port)+'/image'
        r = req.get(url)
        decoder = StolenImageDecoder('<ImageName>')
        ## decoder = StolenImageDecoder('myImage')
        decoder.decodeImage(r.text)


