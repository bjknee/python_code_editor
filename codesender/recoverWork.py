from codesender.serverDB import User, Flask, SQLAlchemy, app, server_db, render_template, request, redirect, url_for
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

# def login():
#     if request.method == 'POST':
#         if request.form['username'] == '' or request.form['password'] == '':
#             return render_template('login.html', loginStatus="Error, no entry.")
#         else:
#             username = request.form['username']
#             password = request.form['password']
#             code_app_user = User.query.filter_by(username=username).first()
#             print(code_app_user)
#             global user_session
#             user_session = username
#             if username == code_app_user.username and password == code_app_user.password:
#                 code = code_app_user.code_seg
#                 return render_template('index.html', username="Logged in as: "+ username, codearea=code)
#             elif username != code_app_user.username or password != code_app_user.password:
#                 return render_template('login.html', loginStatus="Invalid credentials")
#

# @app.route("/login", methods=['POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         loggedIn = False
#         code_app_users = server_db.session.execute(server_db.select(User).order_by(User.username)).scalars()
#         if username not in code_app_users.username:
#             return render_template('login.html', loginStatus="Invalid Username, Please Try Again")
#         else:
#             usersPassword = server_db.session.execute(
#                 server_db.select(User.password).where(User.username == username)).one()
#             if usersPassword != password:
#                 return render_template('login.html', loginStatus="Incorrect Password, Please Try Again")
#             else:
#                 loginStatus = "User: ", username, "Logged In Successfully"
#                 loggedIn = True
#                 if loggedIn:
#                     return render_template('index.html', loginStatus=loginStatus)


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

# @app.route("/login", methods=['POST'])
# def resetPassword():
#     if request.method == 'POST':
#         newPassword1 = request.form['newpassword1']
#         newPassword2 = request.form['newpassword2']

