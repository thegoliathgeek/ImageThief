# Image Thief 
### Note
       Make sure to have opencv installed before using this package.
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


```

