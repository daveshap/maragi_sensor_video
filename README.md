# camera microservice

provides out-of-the-box functionality for robotics and ai in the form of a simple and robust rest api

## requirements

* json
* cv2 (OpenCV)
* sys
* flask

## usage

`python app.py <port: optional/default: 6000>`

Endpoint | Function | Description | Example
--- | --- | --- | ---
/ | GET | Returns default dictionary | `{time: unix epoch, img: numpy ndarray}`
/stereo | GET | Returns stereo dictionary | `{time: unix epoch, left: numpy ndarray, right: numpy ndarry}`
