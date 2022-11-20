from flask import Flask, render_template, request
from subprocess import PIPE, STDOUT, run
from flask_sqlalchemy import SQLAlchemy
from codesender.serverStorage.serverStorage import serverStorage
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
server_db = SQLAlchemy(app)

@app.route("/", methods=['POST', 'GET'])
def index():
    return render_template("index.html")


@app.route("/run_code", methods=['POST', 'GET'])
def run_sender():
    if request.method == 'POST':
        code = request.form['codestuff']
        p = run("python", stdout=PIPE, shell=True, stderr=STDOUT, input=code, encoding='ascii')
        output = p.stdout
        return render_template("index.html", print_output=output, codearea=code)
    else:
        return render_template("index.html")

@app.route("/save_code", methods=['POST'])
def save_code_snippet():
    if request.method == 'POST':
        # --- SAVE SNIPPET INTO DATABASE TO PERSIST ON DIFFERENT SESSIONS ---
        snippet = request.form['codestuff']
        # -------------------------------------------------------------------
        return render_template('index.html', codearea=snippet, savenotification="Code has been saved!")
    else:
        return render_template('index.html')

@app.route("/get_code", methods=['POST'])
def pull_code_snippet():
    if request.method == 'POST':
        # --- SAVE REFERENCE TO CODE SNIPPET FROM DATA BASE IN VAR "snippet" ---
        snippet = "TESTING PULL CODE SNIPPET"
        # ----------------------------------------------------------------------
        return render_template('index.html', codearea=snippet)
    else:
        render_template('index.html')


def main():
    app.run(debug=False)
