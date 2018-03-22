# video_microsvc
generic restful video microservice for AGI
## description
uses USB input devices and provides restful access to real-time images and video
## usage
* start app with optional port number argument
* `python app.py <port>`

Endpoint | Function | Description
--- | --- | ---
/ | GET | Returns default dictionary

## default dictionary
`{time: unix epoch,
  left: numpy ndarray,
  right: numpy ndarry}`
