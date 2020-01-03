# Image Thief 
### Note
       Make sure to have opencv installed before using this package.
### Install
    pip install imagethief

### Dependencies used 
- [Flask](https://github.com/pallets/flask)
- [Requests](https://github.com/psf/requests)
- [OpenCv](https://pypi.org/project/opencv-python/)
## What it's for ?
- Capture image from sever running on default route and get that image over http.
- For example 
    - Assume raspberrypi-1 is running server on *http://192.168.0.2:5000*
    - You wanna get image for raspberry-2 from raspberrypi-1's camera
    - Just use [ImageThief](https://pypi.org/project/ImageThief/) to make things simple.
    
### Server Demo
```python
from ImageThief import Thief

app = Thief(name=__name__)


app.add_plan('/image','image')
app.add_plan('/audio','audio')

app.steal()

```

### Client Demo
```python


```

