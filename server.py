import http.server
import socketserver
import os

PORT = 8000
DIRECTORY = "public"  # Cartella dove si trova index.html

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Server avviato su http://localhost:{PORT}")
    httpd.serve_forever()