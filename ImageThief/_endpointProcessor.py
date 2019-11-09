from flask import Response
from ._imageEncoder import VideoCamera
from base64 import b64encode


class EndpointProcessor(object):

    def __init__(self, action, cameraPort):
        self.action = action
        self.cameraPort = cameraPort

    def __call__(self, *args):
        frame = VideoCamera(self.cameraPort).get_frame()
        self.response = Response(b64encode(frame), status=200)
        self.action()
        return self.response
