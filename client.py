import flask
import requests

cli_port = 6001
srv_port = 6000
srv_end = 'cam'
url = 'http://127.0.0.1:%s/client' % cli_port
app = flask.Flask(__name__)


@app.route("/client", methods=['GET', 'POST'])
def default():
    if flask.request.method == 'POST':
        print(flask.request.form)
        return 'got it thanks!'


def subscribe():
    try:
        response = requests.request('POST',
                                    'http://127.0.0.1:%s/%s' % (srv_port, srv_end),
                                    data={'action': 'subscribe', 'url': url})
        print(response)
    except Exception as exc:
        print(exc)


if __name__ == "__main__":
    subscribe()
    app.run(port=cli_port)


