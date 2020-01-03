from flask import Flask, request, Response
from ._endpointProcessor import EndpointProcessor
from ._globalDict import Data


class Thief(Flask):
    def __init__(self, name=__name__, cameraPort=0):
        super(Thief, self).__init__(name)
        self.cameraPort = cameraPort

    def add_plan(self, endpoint=None, endpoint_name=None, handler=None):
        print(self.test_request_context())
        self.add_url_rule(endpoint, endpoint_name, EndpointProcessor(self.someHandler, self.cameraPort),
                          methods=['POST', 'GET'])

    def steal(self, port=5000, debug=False):
        self.run(host='0.0.0.0', debug=False, port=port)

    def someHandler(self):
        Ext = request.headers.get('Ext', Data.get('Ext', ''))
        Filename = request.headers.get('Filename', Data.get('filename', ''))
        if type(Ext) is unicode:
            Data.update({'Ext': Ext})
        if type(Filename) is unicode:
            Data.update({'filename': Filename})
