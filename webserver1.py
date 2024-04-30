import http.server
import socketserver
import os

# Set the directory to serve files from
web_dir = os.path.join(os.path.dirname(__file__), 'index')
os.chdir(web_dir)

# Define the port number
PORT = 2445

# Create a custom request handler class
class CustomHandler(http.server.SimpleHTTPRequestHandler):
    # Override the log_message method to suppress log messages
    def log_message(self, format, *args):
        pass

# Start the HTTP server
with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print(f"Server started on port {PORT}")
    httpd.serve_forever()

