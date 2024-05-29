#!/usr/bin/python3
""" a simple  http.server for testing"""
import http.server
import json
import socketserver


class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    """Step 1: Create a subclass of http.server.BaseHTTPRequestHandler"""

    def do_GET(self):
        """Step 2: Implement the do_GET method"""
        if self.path == '/data':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode())
        elif self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == '/status':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            error_message = {"error": "Not Found"}
            self.wfile.write(json.dumps(error_message).encode())


"""Step 3: Start the server on a specific port (8000)"""
PORT = 8000

with socketserver.TCPServer(('', PORT), SimpleHTTPRequestHandler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
