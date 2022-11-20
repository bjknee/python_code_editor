# Python 3 server example
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
from subprocess import PIPE, STDOUT, run
from codesender.serverStorage.serverStorage import serverStorage

hostName = "localhost"
serverPort = 8080
db = serverStorage()
global code_reference

class QuizRequestHandler(BaseHTTPRequestHandler):
    """TEMPORARY IMPLEMENTATION OF QUIZ REQUEST HANDLER"""
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(read_template("index.html"), "utf-8"))

    def do_POST(self):
        data_string = self.rfile.read(int(self.headers['Content-Length'])).decode('utf-8')
        data = parse_qs(data_string, keep_blank_values=True)
        global code_reference

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        if self.path == "/run_code":

            code = data['codestuff'][0]
            code_reference = code
            p = run("python", stdout=PIPE, shell=True, stderr=STDOUT, input=code, encoding='ascii')
            output = p.stdout
            new_page = read_template("index.html").replace("<!-- OUTPUT PLACEHOLDER -->", output, 1)
            new_page = new_page.replace("ENTER CODE HERE", code)
            self.wfile.write(bytes(new_page, "utf-8"))

        # ADDS SOME FUNCTIONALITY TO EXPAND PERSISTENT STORAGE MODULE
        if self.path == "/store":
            new_page = read_template("index.html").replace("<!-- OUTPUT PLACEHOLDER -->", " ", 1)
            new_page = new_page.replace("ENTER CODE HERE", "code snippet has been save!")
            self.wfile.write(bytes(new_page, "utf-8"))
            db.storeCode(code_reference, "admin")

        if self.path == "/pull":
            code = db.retrieveCode("admin")
            new_page = read_template("index.html").replace("<!-- OUTPUT PLACEHOLDER -->", "Code has been retrieved", 1)
            new_page = new_page.replace("<!-- OUTPUT_TWO PLACEHOLDER -->", code)
            self.wfile.write(bytes(new_page, "utf-8"))

def read_template(filename, directory='templates'):
    pathname = os.path.join(directory, filename)
    temp_pathname = "codesender/templates/index.html"
    f = open(temp_pathname, "r", encoding="utf-8")
    return f.read()



def main():
    webServer = HTTPServer((hostName, serverPort), QuizRequestHandler)
    print("Server started http://%s:%s" % (hostName, serverPort))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
