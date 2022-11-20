"""
Author: Jalen Blackmore
Group: G Team
Date: November 2, 2022

This module will be implemented for submission 6.

My goal is to work with Kayla's serverStorage module to implement username recognition when a user starts
work in the virtual environment.
    -The interface will be changed to show a "Log In" button that prompts the user to enter their username.
        -This will likely use the checkUser method from serverStorage.
    -Using retrieveCode method, the user will select the previous code that they wish to continue working
    on, and any changes will be saved to the corresponding shelve file.
        -Whether this is done through a command or through a menu of the user's saved code is not yet
        decided.
        -An idea is a dropdown menu of previously saved work that the user can select from.

"""


@app.route("/login", methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        loggedIn = False
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


# @code_app.route("/user/<int:id>/code_seg", methods=["GET", "POST"])
# def add_code(user_id):
#     if request.method == "POST":
#         code_seg = User(
#             username=request.form["username"],
#             code=request.form["code"],
#         )
#         server_db.session.add(code_seg)
#         server_db.session.commit()
#         return redirect(url_for("user_detail", id=user_id))
#
#     return render_template("user/<int:id>/code_seg.html")

@app.route("/login", methods=['POST'])
def resetPassword():
    if request.method == 'POST':
        newPassword1 = request.form['newpassword1']
        newPassword2 = request.form['newpassword2']

