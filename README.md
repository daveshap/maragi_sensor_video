# camera microservice
## usage
`python app.py <port>`

Endpoint | Function | Description
--- | --- | ---
/ | GET | Returns default dictionary
/stereo | GET | Returns stereo dictionary
## default dictionary
`{time: unix epoch, img: numpy ndarray}`
## stereo dictionary
`{time: unix epoch, left: numpy ndarray, right: numpy ndarry}`
