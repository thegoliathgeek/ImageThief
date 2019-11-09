# Image Thief 

### Supports python 3.7+

### Note
       Make sure to have opencv installed before using this package.
### Dependencies used 
- [Flask](https://github.com/pallets/flask)
- [Requests](https://github.com/psf/requests)
- [OpenCv](https://pypi.org/project/opencv-python/)
## What it's for ?
- Capture image from sever running on default route and get that image over http.
- For example 
    - raspberrypi-1 running server on *http://192.168.0.2:5000*
    - You wanna get image for raspberry-2 from raspberrypi-1's camera
    - Just use [ImageThief](https://pypi.org/project/ImageThief/) to make things simple.
    
### Server Demo
```python
from ImageThief import Thief


def some():
    # Do Something here
    print('Image stolen')
    pass


thief = Thief('Dazz', cameraPort=0)
thief.add_plan('/image', 'image', some)
thief.steal(port=3000, debug=True)

```

Client Demo
```python
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
```

