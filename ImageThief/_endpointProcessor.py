from pickle import loads as pickleLoad
from pickle import dumps as pickleDump
from flask import Response


class EndpointProcessor:
    def __init__(self, handler, cameraPort, header=None):
        self.handler = handler
        self.cameraPort = cameraPort
        self.header = header

    def __call__(self, *args, **kwargs):
        self.handler()
        # self.handler(extenstion=self.header.get('ext', ''))
        return Response("OK", status=200)
