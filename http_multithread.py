import http.server
import socketserver
import sys, signal

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

handler_object = MyHttpRequestHandler

PORT = 8080
my_server = socketserver.TCPServer(("", PORT), handler_object)

def signal_handler(signal, frame):
    print( 'Exiting http server (Ctrl+C pressed)')
    try:
      if( my_server ):
        my_server.server_close()
    finally:
      sys.exit(0)
      
signal.signal(signal.SIGINT, signal_handler)

try:
  while True:
    my_server.serve_forever()
except KeyboardInterrupt:
  pass
print( 'Exiting http server (Ctrl+C pressed)')
try:
  if( my_server ):
    my_server.server_close()
finally:
  sys.exit(0)