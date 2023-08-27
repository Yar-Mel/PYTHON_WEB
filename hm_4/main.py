import mimetypes
import urllib.parse
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path
from datetime import datetime


class HttpHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urllib.parse.urlparse(self.path)
        if parsed_url.path == '/':
            self.send_html_file('html/index.html')
        elif parsed_url.path == '/message':
            self.send_html_file('html/message.html')
        else:
            if Path().joinpath(parsed_url.path[1:]).exists():
                # print(parsed_url.path[1:])
                self.send_static()
            else:
                self.send_html_file('html/error.html', 404)

    def do_POST(self):
        data = self.rfile.read(int(self.headers['Content-Length']))
        data_parse = urllib.parse.unquote_plus(data.decode())
        data_dict = {key: value for key, value in [el.split('=') for el in data_parse.split('&')]}
        received_data = dict([(str(datetime.now()), data_dict)])
        # print(received_data)
        if received_data:
            self.write_data(received_data)
        self.send_response(302)
        self.send_header('Location', '/')
        self.end_headers()

    def send_html_file(self, filename, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open(filename, 'rb') as fd:
            self.wfile.write(fd.read())

    def send_static(self):
        self.send_response(200)
        mt = mimetypes.guess_type(self.path)
        if mt:
            self.send_header("Content-type", mt[0])
        else:
            self.send_header("Content-type", 'text/plain')
        self.end_headers()
        with open(f'.{self.path}', 'rb') as file:
            self.wfile.write(file.read())

    def write_data(self, data_dict):
        with open('storage/data.json', 'r') as file:
            try:
                saved_data = json.load(file)
            except json.decoder.JSONDecodeError:
                saved_data = {}
        saved_data.update(data_dict)
        with open('storage/data.json', 'w') as file:
            json.dump(saved_data, file, indent=2)


def run(server_class=HTTPServer, handler_class=HttpHandler):
    server_address = ('', 3000)
    http = server_class(server_address, handler_class)
    try:
        http.serve_forever()
    except KeyboardInterrupt:
        http.server_close()


if __name__ == '__main__':
    run()


