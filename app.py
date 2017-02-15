import os

from flask import Flask, request

from use_models import recognize_image

app = Flask(__name__, static_folder='static', static_url_path='')


@app.route('/mnist', methods=['POST'])
def hello_world():
    score = recognize_image(request.data)
    return str(score[0])


@app.route('/', methods=['GET'])
def index():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
