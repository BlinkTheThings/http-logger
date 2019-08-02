import http.server
import socketserver
import logging

PORT = 8000


class GetHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        logging.error(self.headers)
        http.server.SimpleHTTPRequestHandler.do_GET(self)


with socketserver.TCPServer(("", PORT), GetHandler) as httpd:
    httpd.serve_forever()
