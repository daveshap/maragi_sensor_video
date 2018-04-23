# Stereo Camera Microservice

[MARAGI](https://github.com/benjaminharper2/maragi) Stereo camera vision microservice for the purpose of supporting other microservices such as SLAM and object detection.

## Input

* One or two camera devices

## Output

* JSON serialized numpy ndarray(s) of images

## Requirements

* python3
* flask
* time
* json
* cv2
* threading

## API

Endpoint | Method | Request | Response
--- | --- | --- | ---
`/cam` | GET | Returns mono or stereo image if available | `{time: unix epoch, img0: serialized ndarray, img1: if available}`
`/cam` | POST | `{action: (un)subscribe, url: http://client:port/endpoint}` | Subscribe or unsubscribe request confirmation 
