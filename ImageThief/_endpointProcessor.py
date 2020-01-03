from pickle import dumps as pickleDump
from json import dumps
from flask import Response
from ._globalDict import Data


class EndpointProcessor:
    def __init__(self, handler, cameraPort, header=None):
        self.handler = handler
        self.cameraPort = cameraPort
        self.header = header

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
                return Response(dumps({'data': fl, 'message': 'OK'}), status=200)
