from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
server_db = SQLAlchemy(app)

# @app.route("/", methods=['POST', 'GET'])
# def index():
#     loginStatus = "Not Logged In"
#     return render_template("index.html", loginStatus=loginStatus)
#
# @app.route("/login", methods=['POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         code_app_users = server_db.session.execute(server_db.select(User).order_by(User.username)).scalars()
#         loginStatus = ""
#         if username not in code_app_users.username:
#             loginStatus = "Invalid Username, Please Try Again"
#             return render_template('index.html', loginStatus=loginStatus)
#         else:
#             usersPassword = server_db.session.execute(server_db.select(User.password).where(User.username == username)).one()
#             if usersPassword != password:
#                 loginStatus = "Incorrect Password, Please Try Again"
#                 return render_template('index.html', loginStatus=loginStatus)
#             else:
#                 loginStatus = "User: ", username, "Logged In Successfully"
#                 return render_template('index.html', loginStatus=loginStatus)
#
#
#
#
# @app.route("/get_code", methods=['POST'])
# def pull_code_snippet():
#     if request.method == 'POST':
#         # --- SAVE REFERENCE TO CODE SNIPPET FROM DATA BASE IN VAR "snippet" ---
#         snippet = "TESTING PULL CODE SNIPPET"
#         # ----------------------------------------------------------------------
#         return render_template('index.html', codearea=snippet)
#     else:
#         render_template('index.html')

def main():
    app.run(debug=False)
