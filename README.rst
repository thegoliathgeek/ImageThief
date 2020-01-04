IMAGE THIEF
===============

This is a python library for capturing files over default route (http://0.0.0.0)

Functions:
----------
* Capture files from raspberryPi and access on your system.
* Capture files on one system and access on other.

Installation :
--------------

Python
-------

::

    python -m pip install imagethief --user


Server Demo:
~~~~~~~~~~~~

::

    from ImageThief import Thief

    app = Thief(name=__name__)


    app.add_plan('/image','image')
    app.add_plan('/audio','audio')

    app.steal()


Client Demo:
~~~~~~~~~~~~
::

   from requests import get
    from ImageThief import Decoder as fileSaver

    url = 'http://localhost:5000'
    plan = '/audio'

    a = get(url + plan, headers={'Ext': '.mp3', 'filename': 'sampa.mp3'}).json()

    secondfile = 'some.mp3'
    if a['message'] == 'OK':
        fileSaver(a['data'], secondfile)
        print('File Saved with name ' + secondfile)
    else:
        print('Error')


