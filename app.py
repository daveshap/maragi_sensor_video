import time
import cv2
from flask import Flask
import json
import sys

try:
    cam0 = cv2.VideoCapture(0)
except:
    exit('unable to load a camera')
try:
    cam1 = cv2.VideoCapture(1)
except:
    print('unable to load second camera')


app = Flask(__name__)


@app.route("/")
def default():
    try:
        s, img = cam0.read()
        serialized = str(json.dumps(img.tolist(), separators=(',', ':')))
        return {'time': time.time(), 'img0': serialized}
    except:
        return 'error'

    
@app.route("/stereo")
def default():
    try:
        s, img0 = cam0.read()
        s, img1 = cam1.read()
        serialized0 = str(json.dumps(img0.tolist(), separators=(',', ':')))
        serialized1 = str(json.dumps(img1.tolist(), separators=(',', ':')))
        return {'time': time.time(), 'img0': serialized0, 'img1': serialized1}
    except:
        return 'error'


if __name__ == "__main__":
    if sys.argv[1] is int:
        app.run(port = sys.argv[1])
    else:
        app.run(port=6000)
