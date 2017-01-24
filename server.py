from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from use_mnist import recognize_image

import simplejson

ROUTES = [
    ('/', 'public/')
]


class MyHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        f = open("public/index.html", "r")
        self.wfile.write(f.read())

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        self._set_headers()
        print "in post method"
        length = self.headers['content-length']
        data = self.rfile.read(int(length))

        score = recognize_image(data)


        # self.send_response(200)
        # self.end_headers()
        self.wfile.write(score[0])
        return


def run(server_class=HTTPServer, handler_class=MyHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()


if __name__ == "__main__":
    from sys import argv

if len(argv) == 2:
    run(port=int(argv[1]))
else:
    run()
