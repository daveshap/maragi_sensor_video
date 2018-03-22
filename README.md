# camera microservice

## requirements

* json
* cv2 (OpenCV)
* sys
* flask

## usage

`python app.py <port>`

Endpoint | Function | Description | Example
--- | --- | ---
/ | GET | Returns default dictionary | `{time: unix epoch, img: numpy ndarray}`
/stereo | GET | Returns stereo dictionary | `{time: unix epoch, left: numpy ndarray, right: numpy ndarry}`
