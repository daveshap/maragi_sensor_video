import cv2
from flask import Flask
import json
import sys

cam = cv2.VideoCapture(0)


def snapshot():
    s, img = cam.read()
    return json.dumps(img.tolist(), separators=(',', ':'))


app = Flask(__name__)


@app.route("/")
def default():
    return str(snapshot())


@app.route("/stereo")
def default():
    return str(snapshot())


if __name__ == "__main__":
    if sys.argv[1] is int:
        app.run(port = sys.argv[1])
    else:
        app.run(port=6000)
    #app.run()
