from http.server import HTTPServer, BaseHTTPRequestHandler


with open('index.html', 'r') as file:
    html = file.read()


class WebPhoneBook(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()

        # app1: add 3 users with phone number
        html1 = html.format("""<tr>
                <td align="left">Ana</td>
                <td align="left">007564343</td>
            </tr>""")
        self.wfile.write(html1.encode())


http_server = HTTPServer(('localhost', 8080), WebPhoneBook)
http_server.serve_forever()