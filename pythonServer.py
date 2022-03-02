from http.server import HTTPServer, BaseHTTPRequestHandler
import cgi

#The Handler dealing with GET and POST requests to the server
class Handler(BaseHTTPRequestHandler):

	#Creates the initial page with the form for entering name and submit button
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()
		output = ''
		output += '<html><body><form action ="/hello" method="POST" enctype="multipart/form-data">'
		output += '<label for="name"> Please enter your name: </label><br>'
		output += '<input type="text" id="name" name="name"><br>'
		output += '<input type="submit" name="submit" value="Submit">'
		output += '</form></body></html>'
		self.wfile.write(output.encode())

	#Parses the provided data to return the provided name and prints it with a greeting
	def do_POST(self):
		ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
		#I did not properly understand the purpose of pdict but it was used in the example I was using
		pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
		#finds the provided name based on the field 'name' in the form
		if ctype == 'multipart/form-data':
			fields = cgi.parse_multipart(self.rfile, pdict)
			helloName = fields.get('name')
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()
		successText = ('Hello '+ str(helloName[0]))
		output = ''
		output += '<html><body>'
		output += '<h1 id="success">'
		output += successText
		output += '</h1>'
		output += '</body></html>'
		self.wfile.write(output.encode())

#Creates the server interfacing with port 8080
def main():
	PORT = 8080
	server = HTTPServer(("", PORT), Handler)
	print("Server running on port %s" % PORT)
	server.serve_forever()

if __name__ == '__main__':
	main()