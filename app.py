import cv2
from flask import Flask
import json

cam = cv2.VideoCapture(0)


def snapshot():
    s, img = cam.read()
    return json.dumps(img.tolist(), separators=(',', ':'))


app = Flask(__name__)


@app.route("/")
def default():
    return str(snapshot())


@app.route("/left")
def default():
    return str(snapshot())


@app.route("/right")
def default():
    return str(snapshot())


if __name__ == "__main__":
    app.run()
