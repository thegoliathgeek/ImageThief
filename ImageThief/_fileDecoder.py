from pickle import loads as pickleLoader
from ._globalDict import Data, reExp

import re


def Decoder(unicodeInput, filename, response=None):
    if response is None:
        response = {'extension': ''}
    userExt = re.findall(reExp, filename)[0]
    if userExt != response.get('extension', ''):
        print('Extension doesnt match')
        return
    f = open(filename, 'wb')
    data = pickleLoader(unicodeInput)
    for i in data:
        f.write(i)
    f.close()
