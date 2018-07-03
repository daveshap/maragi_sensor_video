import threading
import cv2
import time
import uuid
import requests
import json
import flask


subscribers = []
app_port = 6001
app_uri = '/cam'
app = flask.Flask(__name__)


def publish_image(img):
    img = str(json.dumps(img.tolist(), separators=(',', ':')))
    t = time.time()
    u = uuid.uuid4()
    payload = {'time': str(t),
               'uuid': str(u),
               'data': img}
    for svc_url in subscribers:
        try:
            requests.request(method='PUT', url=svc_url, json=payload)
        except Exception as exc:
            print(exc)


def cam_thread():
    print('eyeball starting')
    cam = cv2.VideoCapture(0)
    while True:
        s, img = cam.read()
        publish_image(img)
        print('image published!', img.shape)
        time.sleep(1)


@app.route(app_uri, methods=['POST'])
def default():
    request = flask.request
    payload = json.loads(request.data)
    print(payload)
    if request.method == 'POST':
        if payload['action'] == 'subscribe':
            if payload['url'] not in subscribers:
                subscribers.append(payload['url'])
                return json.dumps({'result': 'successfully added URL to subscribers list'})
            else:
                return json.dumps({'result': 'URL was already in subscribers list'})


if __name__ == "__main__":
    threading.Thread(target=cam_thread).start()
    app.run(port=app_port)
