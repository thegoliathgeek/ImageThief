import cv2
from base64 import b64decode
import numpy as np


class StolenImageDecoder:
    def __init__(self, name):
        self.name = name

    def decodeImage(self, frame):
        decodedPayload = b64decode(frame)
        np_arr = np.fromstring(decodedPayload, np.uint8)
        cv2_img = cv2.imdecode(np_arr, 1)
        cv2.imwrite(self.name + '.jpg', cv2_img)
