import cv2
import time
import uuid
import requests
import json


directory = 'http://127.0.0.1:5000/directory'


def publish_audio(img, phonebook):
    t = time.time()
    u = uuid.uuid4()
    payload = {'time': str(t),
               'uuid': str(u),
               'type': 'raw_video',
               'source': 'camera service',
               'data': img}
    for service in phonebook:
        try:
            if service['input'] == 'raw_audio':
                print('POST to', service)
                response = requests.request(method='PUT', url=service['svc_url'], json=payload)
                print(response)
        except Exception as exc:
            print(exc)


def get_phonebook():
    response = requests.request(method='GET', url=directory)
    text = response.text
    phonebook = json.loads(text)
    return phonebook


if __name__ == "__main__":
    print('eyeballs starting')
    cam = cv2.VideoCapture(0)
    while True:
        time.sleep(1)
        s, img = cam.read()
        img = str(json.dumps(img.tolist(), separators=(',', ':')))
        phonebook = get_phonebook()