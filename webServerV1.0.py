from BaseHttpSeerver import HTTPServer, BaseHTTPRequestHandler
class TestHTTPHandle(BaseHTTPRequestHandler):
	def do_GET(self):
		buf = 'It works'
		self.protocal_version = "HTTP/1.1"
		self.send_response(200)
		self.send_header("Welcome", "Contect")
		self.end_headers()
		self.wfile.write(buf)

def start_server(port):
	http_server = HTTPServer(('172.0.0.1', int(port)), TestHTTPHandler)
	http_server.serve_forever()