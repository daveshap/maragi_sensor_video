import flask
import json
import requests


directory_url = 'http://127.0.0.1:5000/directory'
app = flask.Flask(__name__)                                     # flask app
app_port = 8999                                                 # port for this service to run on
app_uri = "/test"                                               # uri endpoint
app_ip = "127.0.0.1"                                            # ip address of local machine
app_url = "http://%s:%s%s" % (app_ip, app_port, app_uri)        # receiving url


@app.route(app_uri, methods=["PUT", "GET"])
def default():
    payload = json.loads(flask.request.data)
    print(payload)
    return json.dumps({'result': 'got it!'})


if __name__ == '__main__':
    service = {'name': 'test video service',
               'input': 'raw_video',
               'output': 'video_tests',
               'svc_ip': app_ip,
               'svc_port': app_port,
               'svc_uri': app_uri,
               'svc_url': app_url}
    payload = {'service': service}
    print('REGISTER', payload)
    response = requests.request(method='PUT', url=directory_url, json=payload)
    print('RESPONSE', response)
    app.run(port=app_port)
