from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs


import endpoints
import json
from endpoints import *

host = 'localhost'
port = 80

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        #query_params = parse_qs(parsed_url.query)
        path = (parsed_url[2])
        #user_id = int(query_params.get('user_id')[0])
        '''if path == "/repetition":
            response_user = endpoints.get_repetition(user_id)
            self.send_response(200)
            self.wfile.write(f"{response_user}".encode())'''
        if path == "/api/v1/on": #для реле вкл
            message_response = 'OK'
            self.send_response(200, message=message_response)
            self.protocol_version = 'HTTP/1.1'
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            message = 'OUT'
            self.wfile.write(message.encode('utf-8'))
        elif path == '/api/v1/off': #для реле выкл
            self.send_response(200)
            self.wfile.write(b'IN')


if __name__ == '__main__':
    httpd = HTTPServer((host, port), MyHandler)
    print('Server started http://%s:%s' % (host, port))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()



'''class HandlerGet(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        #self.send_header("Content-type", "text/html")
        self.end_headers()
        #self.wfile.write("hello Rolu".encode())
        self.path = "/logic"
        """# If someone went to "http://something.somewhere.net/foo/bar/",
        # then s.path equals "/foo/bar/".
        self.wfile.write("<p>You accessed path: %s</p>" % self.path)
        self.wfile.write("</body></html>")"""

def run(handler_class=BaseHTTPRequestHandler):
    server = HTTPServer((host, port), handler_class)
    """hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print(local_ip)"""
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()

run(handler_class=HandlerGet)'''


'''connection = http.client.HTTPSConnection("localhost:80")
connection.request("GET", "/logic")
response = connection.getresponse()'''