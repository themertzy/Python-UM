
# A simple http server for web development.

# Run this program in the directory of the website you want to serve to the local host.

import http.server

import socketserver


PORT = 8080

Handler = http.server.SimpleHTTPRequestHandler


with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("serving at port", PORT)

    httpd.serve_forever()
