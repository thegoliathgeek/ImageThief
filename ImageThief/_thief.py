from flask import Flask
from ._endpointProcessor import EndpointProcessor


class Thief:
    def __init__(self, name, cameraPort):
        self.app = Flask(name)
        self.cameraPort = cameraPort

    def add_plan(self, endpoint=None, endpoint_name=None, handler=None):
        self.app.add_url_rule(endpoint, endpoint_name, EndpointProcessor(handler, self.cameraPort))

    def steal(self, port=5000, debug=False):
        self.app.run(host='0.0.0.0', debug=False, port=port)

# class Thief():
#     def __init__(self):
#         pass
#
#     @app.route('/')
#     def index(self):
#         return "<h1> Up and Running</h1>"
#
#     def gen(self, camera):
#         while True:
#             frame = camera.get_frame()
#             return frame
#
#     @app.route('/image')
#     def image_steal(self):
#         k = self.gen(VideoCamera())
#         return Response(b64encode(k), headers={'name': 'Dhanush'})
#
#
#     @app.route('/hello')
#     def hello_w(self):
#         print(request.headers.get('data'))
#         return "<h1> Hello World </h1>"
#
#     def steal(self):
#         app.run(host='0.0.0.0', debug=True)
