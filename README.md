# Basic Camera Microservice

Basic camera service that publishes one image per second to subscribed services. 

# API

The REST API for this microservice is described below

Attribute | Value
--- | ---
URI | /cam
Port | 6001
Methods | POST

# Payload

The JSON payload should be a dictionary with the following element(s)

Element | Required | Value(s)
--- | --- | ---
action | true | Only accepts `subscribe`
url | true | full service URL for where images are to be sent. Ex `http://127.0.0.1:5555/client`

# Output

Publishes one image per second to all URLs in the `subscribers` list

Field | Description
--- | ---
time | unix epoch timestamp
uuid | uuid v4 identifier for sample
data | JSON serialized ndarray of an image
