from subprocess import PIPE, STDOUT, run
from codesender.serverDB import User, Flask, SQLAlchemy, app, server_db, render_template, request, redirect, url_for
global user_session


"""--- FLASK FRAMEWORK ENDPOINT ROUTING MODULE ---"""


@app.route("/", methods=['POST', 'GET'])
def index():
    return render_template("login.html")

@app.route("/run_code", methods=['POST', 'GET'])
def run_sender():
    if request.method == 'POST':
        code = request.form['codestuff']
        p = run("python", stdout=PIPE, shell=True, stderr=STDOUT, input=code, encoding='ascii')
        output = p.stdout
        return render_template("index.html", print_output=output, codearea=code, username="Logged in as: "+user_session)
    else:
        return render_template("index.html")


"""------------------------------------------------"""

""" --- USER LOGIN AND PASSWORDS MODULE --- """


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
            if code_app_user == None:
                return render_template('login.html', loginStatus="Invalid credentials")
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


"""-----------------------------------------"""


"""--- SAVE-REVERT BUTTONS MODULE ---"""


@app.route("/save_code", methods=["GET", "POST"])
def add_code():
    if request.method == "POST":
        global user_session
        code_app_user = User.query.filter_by(username=user_session).first()
        code = request.form['codestuff']
        code_app_user.code_seg = code
        server_db.session.commit()
        print(code_app_user.code_seg)
        return render_template("index.html", codearea=code, username="Logged in as: "+user_session)



@app.route("/get_code", methods=['POST'])
def pull_code_snippet():
    if request.method == 'POST':
        global user_session
        code_app_user = User.query.filter_by(username=user_session).first()
        code = code_app_user.code_seg
        return render_template('index.html', codearea=code, username="Logged in as: "+user_session)
    else:
        return render_template('index.html')


"""-----------------------------------------"""


""" --- PERSONAL CODE SPACES MODULE ---"""


@app.route("/return_to_index", methods=['POST'])
def return_to_index():
    if request.method == 'POST':
        code_app_user = User.query.filter_by(username=user_session).first()
        code = code_app_user.code_seg
        return render_template('index.html', username="Logged in as: "+ user_session, codearea=code)


@app.route("/personal_run_one", methods=['POST'])
def run_profile_one():
    if request.method == 'POST':
        code = request.form['codestuff']
        p = run("python", stdout=PIPE, shell=True, stderr=STDOUT, input=code, encoding='ascii')
        output = p.stdout
        return render_template("profileOne.html", print_output=output, codearea=code, username=user_session+"'s Code Space 1")
    else:
        return render_template("login.html", loginstatus="Something went wrong.")


@app.route("/personal_run_two", methods=['POST'])
def run_profile_two():
    if request.method == 'POST':
        code = request.form['codestuff']
        p = run("python", stdout=PIPE, shell=True, stderr=STDOUT, input=code, encoding='ascii')
        output = p.stdout
        return render_template("profileTwo.html", print_output=output, codearea=code, username=user_session+"'s Code Space 2")
    else:
        return render_template("login.html", loginstatus="Something went wrong.")


@app.route("/personal_run_three", methods=['POST'])
def run_profile_three():
    if request.method == 'POST':
        code = request.form['codestuff']
        p = run("python", stdout=PIPE, shell=True, stderr=STDOUT, input=code, encoding='ascii')
        output = p.stdout
        return render_template("profileThree.html", print_output=output, codearea=code, username=user_session+"'s Code Space 3")
    else:
        return render_template("login.html", loginstatus="Something went wrong.")


@app.route("/profileOne", methods=['POST'])
def profileOne():
    if request.method == 'POST':
        code_app_user = User.query.filter_by(username=user_session).first()
        code = code_app_user.personal_code_one
        return render_template("profileOne.html", codearea=code, username=user_session+"'s Code Space 1")

@app.route("/profileTwo", methods=['POST'])
def profileTwo():
    if request.method == 'POST':
        code_app_user = User.query.filter_by(username=user_session).first()
        code = code_app_user.personal_code_two
        return render_template("profileTwo.html", codearea=code, username=user_session + "'s Code Space 2")

@app.route("/profileThree", methods=['POST'])
def profileThree():
    if request.method == 'POST':
        code_app_user = User.query.filter_by(username=user_session).first()
        code = code_app_user.personal_code_three
        return render_template("profileThree.html", codearea=code, username=user_session + "'s Code Space 3")


@app.route("/save_profile_one", methods=['POST'])
def saveProfileOne():
    if request.method == "POST":
        global user_session
        code_app_user = User.query.filter_by(username=user_session).first()
        code = request.form['codestuff']
        code_app_user.personal_code_one = code
        server_db.session.commit()
        return render_template("profileOne.html", codearea=code, savenotification="Code Saved to Profile 1!", username=user_session + "'s Code Space 1")

@app.route("/save_profile_two", methods=['POST'])
def saveProfileTwo():
    if request.method == "POST":
        global user_session
        code_app_user = User.query.filter_by(username=user_session).first()
        code = request.form['codestuff']
        code_app_user.personal_code_two = code
        server_db.session.commit()
        return render_template("profileTwo.html", codearea=code, savenotification="Code Saved to Profile 2!", username=user_session + "'s Code Space 2")

@app.route("/save_profile_three", methods=['POST'])
def saveProfileThree():
    if request.method == "POST":
        global user_session
        code_app_user = User.query.filter_by(username=user_session).first()
        code = request.form['codestuff']
        code_app_user.personal_code_three = code
        server_db.session.commit()
        return render_template("profileThree.html", codearea=code, savenotification="Code Saved to Profile 3!", username=user_session + "'s Code Space 3")



"""------------------------------------"""


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


def main():
    with app.app_context():
        server_db.create_all()
    app.run(debug=True)
