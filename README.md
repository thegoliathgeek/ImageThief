# Image Thief 

### Install
    pip install imagethief

### Dependencies used 
- [Flask](https://github.com/pallets/flask)
- [Requests](https://github.com/psf/requests)

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



import requests as req
from ImageThief import StolenImageDecoder

if __name__ == '__main__':
        your_ip = '<your server ip>'
        port = 5000 #default
        url = 'http://'+your_ip+':'+str(port)+'/plan_name'
        # For above Demo code (Server Demo)  it is
        # url = 'http://'+your_ip+':'+str(port)+'/image'
        r = req.get(url)
        decoder = StolenImageDecoder('<ImageName>')
        ## decoder = StolenImageDecoder('myImage')
        decoder.decodeImage(r.text)
```

