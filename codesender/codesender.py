from flask import Flask, render_template, request
from subprocess import PIPE, STDOUT, run
from flask_sqlalchemy import SQLAlchemy


from codesender.serverStorage.serverStorage import serverStorage
import os

from codesender.serverStorage.serverDB import User, Admin

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
server_db = SQLAlchemy(app)

@app.route("/", methods=['POST', 'GET'])
def index():
    return render_template("login.html")

@app.route("/run_code", methods=['POST', 'GET'])
def run_sender():
    if request.method == 'POST':
        code = request.form['codestuff']
        p = run("python", stdout=PIPE, shell=True, stderr=STDOUT, input=code, encoding='ascii')
        output = p.stdout
        return render_template("index.html", print_output=output, codearea=code)
    else:
        return render_template("index.html")

@app.route("/login", methods=['POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == '' or request.form['password'] == '':
            return render_template('login.html', loginStatus="Error, no entry.")
        else:
            username = request.form['username']
            password = request.form['password']
            code_app_users = server_db.session.execute(server_db.select(User).order_by(User.username)).scalars()
            if username not in code_app_users.username:
                return render_template('login.html', loginStatus="Invalid Username, Please Try Again")
            else:
                usersPassword = server_db.session.execute(
                    server_db.select(User.password).where(User.username == username)).one()
                if usersPassword != password:
                    return render_template('login.html', loginStatus="Incorrect Password, Please Try Again")
                else:
                    loginStatus = "User: ", username, "Logged In Successfully"
                    loggedIn = True
                    if loggedIn:
                        return render_template('index.html', loginStatus=loginStatus)

@app.route("/create-user", methods=["GET", "POST"])
def user_create():
    if request.method == "POST":
        user = User(
            username=request.form["username"],
            password=request.form["password"],
        )
        server_db.session.add(user)
        server_db.session.commit()
        return render_template("index.html", savenotification=user.username)


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
    with app.app_context():
        server_db.create_all()
    app.run(debug=True)
