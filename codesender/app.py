from flask import Flask, render_template, request, redirect
from subprocess import PIPE, STDOUT, run
import os

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def index():
    return render_template("index.html")


@app.route("/run_code", methods=['POST', 'GET'])
def run_sender():
    if request.method == 'POST':
        code = request.form['codestuff']
        p = run("python", stdout=PIPE, shell=True, stderr=STDOUT, input=code, encoding='ascii')
        output = p.stdout
        new_page = read_template("index.html").replace("<!-- OUTPUT PLACEHOLDER -->", output, 1)
        new_page = new_page.replace("ENTER CODE HERE", code)
        return (new_page)
    else:
        return render_template("index.html")


def read_template(filename, directory='templates'):
    pathname = os.path.join(directory, filename)
    temp_pathname = "codesender/templates/index.html"
    f = open(pathname, "r", encoding="utf-8")
    return f.read()


def main():
    app.run(debug=False)

main()