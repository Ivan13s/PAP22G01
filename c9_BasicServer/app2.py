from http.server import HTTPServer, BaseHTTPRequestHandler
from bs4 import BeautifulSoup


with open('index.html', 'r') as file:
    soup = BeautifulSoup(file, "html.parser")
    obiect = soup.find('table')
    obiect.new_tag('tr')
    print(obiect)
    # print(soup)
class WebPhoneBook(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        # html1 = html.replace('{}', """    <tr>
#     <td align="left">John</td>
#     <td align="left">112</td>
# </tr>""")
        # app1: add 3 users with phone number
        # self.wfile.write(soup.encode())
        http_server = HTTPServer(('localhost', 8080), WebPhoneBook)
        http_server.serve_forever()