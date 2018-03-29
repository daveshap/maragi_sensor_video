# Stereo Camera Microservice

[MARAGI](https://github.com/benjaminharper2/maragi) Stereo camera vision microservice for the purpose of supporting other microservices such as SLAM and object detection.

## Input

* One or two cameras

## Output

* JSON serialized numpy ndarray(s) of images

## Requirements

* python3
* flask
* time
* json
* sys
* cv2

## API

Endpoint | Method | Request | Response
--- | --- | --- | ---
`/` | GET | Returns default dictionary | `{time: unix epoch, img0: serialized ndarray}`
`/stereo` | GET | Returns stereo dictionary | `{time: unix epoch, img0: serialized ndarray, img1: serialized ndarray}`
