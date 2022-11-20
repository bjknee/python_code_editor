from subprocess import PIPE, STDOUT, run
from codesender.serverDB import User, Flask, SQLAlchemy, app, server_db, render_template, request, redirect, url_for
global user_session

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

# TODO: Handle all use cases for user input
@app.route("/login", methods=['POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == '' or request.form['password'] == '':
            return render_template('login.html', loginStatus="Error, no entry.")
        else:
            username = request.form['username']
            password = request.form['password']
            code_app_user = User.query.filter_by(username=username).first()
            print(code_app_user)
            global user_session
            user_session = username
            if username == code_app_user.username and password == code_app_user.password:
                code = code_app_user.code_seg
                return render_template('index.html', username="Logged in as: "+ username, codearea=code)
            elif username != code_app_user.username or password != code_app_user.password:
                return render_template('login.html', loginStatus="Invalid credentials")

# TODO: Handle duplicate entry values
@app.route("/create-user", methods=["GET", "POST"])
def user_create():
    if request.method == "POST":
        user = User(
            username=request.form["username"],
            password=request.form["password"],
        )
        server_db.session.add(user)
        server_db.session.commit()
        print(user)
        global user_session
        user_session = user.username
        return render_template("index.html", username="Logged in as: "+user.username)

#TODO: Future functionality

# @app.route("/users")
# def user_list():
#     code_app_users = server_db.session.execute(server_db.select(User).order_by(User.username)).scalars()
#     return render_template("user/list.html", users=code_app_users)
#
#
# @app.route("/user/<int:id>")
# def user_detail(usr_id):
#     user = server_db.get_or_404(User, usr_id)
#     return render_template("user/detail.html", user=user)
#
#
# @app.route("/user/<int:id>/delete", methods=["GET", "POST"])
# def user_delete(usr_id):
#     user = server_db.get_or_404(User, usr_id)
#
#     if request.method == "POST":
#         server_db.session.delete(user)
#         server_db.session.commit()
#         return redirect(url_for("user_list"))
#
#     return render_template("user/delete.html", user=user)


@app.route("/save_code", methods=["GET", "POST"])
def add_code():
    if request.method == "POST":
        global user_session
        code_app_user = User.query.filter_by(username=user_session).first()
        code = request.form['codestuff']
        code_app_user.code_seg = code
        server_db.session.commit()
        print(code_app_user.code_seg)
        return render_template("index.html")



@app.route("/get_code", methods=['POST'])
def pull_code_snippet():
    if request.method == 'POST':
        global user_session
        code_app_user = User.query.filter_by(username=user_session).first()
        code = code_app_user.code_seg
        return render_template('index.html', codearea=code)
    else:
        return render_template('index.html')

# STUB IMPLEMENTATION
@app.route("/personal_code", methods=['POST'])
def personal_codespace():
    if request.method == 'POST':
        return render_template('profiles.html', username=user_session)


def main():
    with app.app_context():
        server_db.create_all()
    app.run(debug=True)
