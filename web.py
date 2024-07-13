import SimpleHTTPServer
import SocketServer
# import ssl
import os



host = "0.0.0.0"
port = 80
web_dir = "sanitized"
cd = os.chdir(web_dir)
print os.getcwd()

Handler   = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd     = SocketServer.TCPServer((host, port), Handler)
httpd     = httpd.serve_forever()
