from pickle import loads as pickleLoader

def Decoder(unicodeInput, filename):
    f = open(filename, 'wb')
    data =  pickleLoader(unicodeInput)
    for i in data:
        f.write(i)
    f.close()
