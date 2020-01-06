from pickle import dumps as pickleDump
from json import dumps
from flask import Response
from ._globalDict import Data
import socket




class EndpointProcessor:
    def __init__(self, handler, cameraPort, header=None):
        self.handler = handler
        self.cameraPort = cameraPort
        self.header = header

    def GetCurrentIp(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(('10.255.255.255', 1))
            IP = s.getsockname()[0]
        except:
            IP = '127.0.0.1'
        finally:
            s.close()
        return IP


    def __call__(self, *args, **kwargs):
        self.handler()
        ext = Data.get('Ext', None)
        if ext == None:
            return Response(dumps({'message': 'Not Found extension'}), status=404)
        else:
            txtFile = Data.get('filename', None)
            if txtFile == None:
                return Response(dumps({'message': 'Not Found text file'}), status=404)
            else:
                f = open(txtFile, 'rb')
                fl = pickleDump(f.readlines())
                f.close()
                return Response(dumps({'data': fl, 'message': 'OK', 'extension': ext, "IP": self.GetCurrentIp()}), status=200)
