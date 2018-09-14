import pika
import cv2
import json
import time


def publish_video():
    cam = cv2.VideoCapture(0)
    parameters = pika.URLParameters('amqp://guest:guest@maragi-rabbit:5672/%2F')
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    print('AMQP connection established and camera is active')
    while True:
        s, img = cam.read()
        img = str(json.dumps(img.tolist(), separators=(',', ':')))
        channel.basic_publish(exchange='sensor_video', body=img, routing_key='')
        time.sleep(0.25)


if __name__ == '__main__':
    while True:
        try:
            publish_video()
        except Exception as oops:
            print('ERROR:', oops)