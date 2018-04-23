import time
import cv2
import flask
import json
import threading
import requests

#           open cv stuff

try:
    cam0 = cv2.VideoCapture(0)
except:
    exit('unable to load a camera')
try:
    cam1 = cv2.VideoCapture(1)
except:
    print('unable to load second camera')

#           flask stuff

subscribers = []    # list of urls to post sounds to
port = 6000         # this needs to be a system argument
frequency = 2       # frequency in seconds to update subscribers by default
app = flask.Flask(__name__)


def snapshot():
    try:
        s, img = cam0.read()
        img0 = str(json.dumps(img.tolist(), separators=(',', ':')))
        s, img = cam1.read()
        img1 = str(json.dumps(img.tolist(), separators=(',', ':')))
        obj = {'img0': img0, 'img1': img1, 'time': time.time()}
        return obj

    except:
        s, img = cam0.read()
        img0 = str(json.dumps(img.tolist(), separators=(',', ':')))
        obj = {'img0': img0, 'time': time.time()}
        return obj


def subscriber_thread():
    while True:
        time.sleep(2)
        for sub in subscribers:
            try:
                response = requests.request('POST', sub, data=snapshot())
                print('POST to', sub, response.status_code)
            except Exception as exc:
                print(exc)


@app.route("/cam", methods=['GET', 'POST'])
def default():

    if flask.request.method == 'GET':
        return snapshot()

    elif flask.request.method == 'POST':
        post = flask.request.form
        print(post)

        try:

            if post['action'] == 'subscribe':
                sub = post['url']
                if sub in subscribers:
                    return 'already subscribed!'
                else:
                    subscribers.append(sub)
                    return 'subscribed'

            elif post['action'] == 'unsubscribe':
                sub = post['url']
                if sub in subscribers:
                    subscribers.remove(sub)
                    return 'unsubscribed'
                else:
                    return 'not a subscriber'

        except Exception as exc:
            return str(exc)


if __name__ == "__main__":
    sub_thread = threading.Thread(target=subscriber_thread)
    sub_thread.start()
    app.run(port=6000)
