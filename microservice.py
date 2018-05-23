import threading
import cv2
import time
import uuid
import requests
import json


directory = 'http://127.0.0.1:5000/directory'
phonebook = []


def publish_image(img):
    global phonebook
    img = str(json.dumps(img.tolist(), separators=(',', ':')))
    t = time.time()
    u = uuid.uuid4()
    payload = {'time': str(t),
               'uuid': str(u),
               'type': 'raw_video',
               'source': 'camera service',
               'data': img}
    for service in phonebook:
        try:
            if service['input'] == 'raw_video':
                print('POST to', service)
                response = requests.request(method='PUT', url=service['svc_url'], json=payload)
                print(response)
        except Exception as exc:
            print(exc)


def get_phonebook():
    # periodically updates the phonebook
    global phonebook
    while True:
        response = requests.request(method='GET', url=directory)
        text = response.text
        phonebook = json.loads(text)
        time.sleep(60)


if __name__ == "__main__":
    print('eyeball starting')
    cam = cv2.VideoCapture(0)
    phonebook_updater = threading.Thread(target=get_phonebook)
    phonebook_updater.start()
    while True:
        s, img = cam.read()
        publisher = threading.Thread(target=publish_image(img))
        publisher.start()
        time.sleep(1)
