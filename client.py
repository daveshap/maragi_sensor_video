import flask
import json
import requests
import numpy as np


app = flask.Flask(__name__)                                     # flask app
app_port = 9999                                                 # port for this service to run on
app_uri = '/test'                                               # uri endpoint
app_ip = '127.0.0.1'                                            # ip address of local machine
app_url = 'http://%s:%s%s' % (app_ip, app_port, app_uri)        # receiving url
svc_url = 'http://127.0.0.1:6001/cam'


@app.route(app_uri, methods=['PUT', 'GET'])
def default():
    payload = json.loads(flask.request.data)
    img = json.loads(payload['data'])
    img = np.asarray(img)
    print(payload['uuid'], payload['time'], img.shape)
    return json.dumps({'result': 'client successfully received'})


if __name__ == '__main__':
    response = requests.request(method='POST', url=svc_url, json={'action': 'subscribe', 'url': app_url})
    print('RESPONSE', response)
    app.run(port=app_port)
