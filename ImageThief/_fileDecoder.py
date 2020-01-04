from pickle import loads as pickleLoader
from ._globalDict import Data, reExp

import re


def Decoder(unicodeInput, filename):

    userExt = re.findall(reExp, filename)
    if userExt != Data.get('Ext',''):
        print('Extension doesnt match')
        return
    f = open(filename, 'wb')
    data = pickleLoader(unicodeInput)
    for i in data:
        f.write(i)
    f.close()
