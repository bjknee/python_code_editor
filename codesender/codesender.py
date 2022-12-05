from subprocess import PIPE, STDOUT, run
from codesender.serverDB import User, Admin, Flask, SQLAlchemy, app, server_db, render_template, request, redirect, \
    url_for

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
        return render_template("index.html", print_output=output, codearea=code,
                               username="Logged in as: " + user_session)
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
                return render_template('index.html', username="Logged in as: " + username, codearea=code)

            elif username != code_app_user.username or password != code_app_user.password:
                return render_template('login.html', loginStatus="Invalid credentials")


# admin login
@app.route("/adminPage", methods=["POST"])
def adminAccess():
    if request.method == 'POST':
        if request.form['username'] == '' or request.form['password'] == '':
            return render_template('login.html', loginStatus="Error, wrong entry.")
        else:
            print("admin login")
            if request.form["username"].startswith("admin"):
                adminName = request.form["username"]
                code_app_admin = Admin.query.filter_by(admin_name=adminName).first()
                if code_app_admin == None:
                    return render_template("login.html", loginStatus1="Invalid credentials")

                if code_app_admin.admin_pass == request.form["password"]:
                    return render_template("adminPage.html", username="Logged in as an admin, " + adminName)

                else:
                    return render_template("adminPage.html", username="Invalid credentials " + adminName)

    return


@app.route("/saveChanges", methods=["POST"])
def adminChangeCode():
    selectedUsr = request.form["userSelected"]
    usrObj = User.query.filter_by(username=selectedUsr).first()

    if selectedUsr == "Enter username to make changes" or selectedUsr.startswith("admin") \
            or usrObj == None:  # nonetype has no attribute error
        return render_template("adminPage.html", loginSt="Invalid credentials")
    else:
        print("else")
        print(selectedUsr)
        print(request.form["codeToChange1"])
        if request.form["codeToChange1"] != "Enter code for codespace 1 to make changes":
            usrObj.personal_code_one = request.form["codeToChange1"]
            server_db.session.commit()

        if request.form["codeToChange2"] != "Enter code for codespace 2 to make changes":
            usrObj.personal_code_two = request.form["codeToChange2"]
            server_db.session.commit()

        if request.form["codeToChange3"] != "Enter code for codespace 3 to make changes":
            usrObj.personal_code_three = request.form["codeToChange3"]
            server_db.session.commit()
        return render_template("adminPage.html", loginSt="changes are saved!")


# TODO: Handle duplicate entry values
@app.route("/create-user", methods=["GET", "POST"])
def user_create():
    if request.method == "POST":
        boolean = request.form["username"].startswith("admin")
        if boolean:
            if request.form["password"] == None:
                return render_template("login.html", error="wrong entry")
            admin = Admin(
                admin_name=request.form["username"],
                admin_pass=request.form["password"],
            )
            server_db.session.add(admin)
            server_db.session.commit()
            return render_template("adminPage.html", username="Logged in as an admin, " + admin.admin_name)

        if request.form["username"] == "" or request.form["password"] == "":
            return render_template("login.html", error="no entry")
        else:
            user = User(
                username=request.form["username"],
                password=request.form["password"],
            )

            server_db.session.add(user)
            server_db.session.commit()
            print(user)
            global user_session
            user_session = user.username
            return render_template("index.html", username="Logged in as: " + user.username)


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
        return render_template("index.html", codearea=code, username="Logged in as: " + user_session)


@app.route("/get_code", methods=['POST'])
def pull_code_snippet():
    if request.method == 'POST':
        global user_session
        code_app_user = User.query.filter_by(username=user_session).first()
        code = code_app_user.code_seg
        return render_template('index.html', codearea=code, username="Logged in as: " + user_session)
    else:
        return render_template('index.html')


"""-----------------------------------------"""

""" --- PERSONAL CODE SPACES MODULE ---"""


@app.route("/adminChanges", methods=["POST"])
def adminSelectsUser():
    if request.method == "POST":
        selectedUsername = request.form["userSelected"]
        selection = User.query.filter_by(username=selectedUsername).first()
        if selection != None:
            return render_template("adminChanges.html", message="selected user: " + selection.username)
        else:
            return render_template("adminChanges.html", message="User not found!")


@app.route("/return_to_index", methods=['POST'])
def return_to_index():
    if request.method == 'POST':
        code_app_user = User.query.filter_by(username=user_session).first()
        code = code_app_user.code_seg
        return render_template('index.html', username="Logged in as: " + user_session, codearea=code)


@app.route("/personal_run_one", methods=['POST'])
def run_profile_one():
    if request.method == 'POST':
        code = request.form['codestuff']
        p = run("python", stdout=PIPE, shell=True, stderr=STDOUT, input=code, encoding='ascii')
        output = p.stdout
        return render_template("profileOne.html", print_output=output, codearea=code,
                               username=user_session + "'s Code Space 1")
    else:
        return render_template("login.html", loginstatus="Something went wrong.")


@app.route("/personal_run_two", methods=['POST'])
def run_profile_two():
    if request.method == 'POST':
        code = request.form['codestuff']
        p = run("python", stdout=PIPE, shell=True, stderr=STDOUT, input=code, encoding='ascii')
        output = p.stdout
        return render_template("profileTwo.html", print_output=output, codearea=code,
                               username=user_session + "'s Code Space 2")
    else:
        return render_template("login.html", loginstatus="Something went wrong.")


@app.route("/personal_run_three", methods=['POST'])
def run_profile_three():
    if request.method == 'POST':
        code = request.form['codestuff']
        p = run("python", stdout=PIPE, shell=True, stderr=STDOUT, input=code, encoding='ascii')
        output = p.stdout
        return render_template("profileThree.html", print_output=output, codearea=code,
                               username=user_session + "'s Code Space 3")
    else:
        return render_template("login.html", loginstatus="Something went wrong.")


@app.route("/profileOne", methods=['POST'])
def profileOne():
    global user_session
    if request.method == 'POST':
        code_app_user = User.query.filter_by(username=user_session).first()
        code = code_app_user.personal_code_one
        return render_template("profileOne.html", codearea=code, username=user_session + "'s Code Space 1")


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
        return render_template("profileOne.html", codearea=code, savenotification="Code Saved to Profile 1!",
                               username=user_session + "'s Code Space 1")


@app.route("/save_profile_two", methods=['POST'])
def saveProfileTwo():
    if request.method == "POST":
        global user_session
        code_app_user = User.query.filter_by(username=user_session).first()
        code = request.form['codestuff']
        code_app_user.personal_code_two = code
        server_db.session.commit()
        return render_template("profileTwo.html", codearea=code, savenotification="Code Saved to Profile 2!",
                               username=user_session + "'s Code Space 2")


@app.route("/save_profile_three", methods=['POST'])
def saveProfileThree():
    if request.method == "POST":
        global user_session
        code_app_user = User.query.filter_by(username=user_session).first()
        code = request.form['codestuff']
        code_app_user.personal_code_three = code
        server_db.session.commit()
        return render_template("profileThree.html", codearea=code, savenotification="Code Saved to Profile 3!",
                               username=user_session + "'s Code Space 3")


"""------------------------------------"""


# TODO: Future functionality

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
