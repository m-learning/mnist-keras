import os

from flask import Flask, request

from use_mnist import recognize_image

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        score = recognize_image(request.data)
        print score
        return str(score[0])
    else:
        return app.send_static_file('index.html')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
