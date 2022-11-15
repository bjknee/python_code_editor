from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

"""
Author: Kayla Malcolm, CS 2005 G Team
Cycle Initiation: Cycle 6
This module serves a revision to the serverStorage module, by incorporating a database storage method as opposed to the
serverStorage module's use of Shelve. This is to provide a much more robust means of storing user profiles and 
codespaces, as well as a storage solution that can be scaled much more easily.
"""

server_db = SQLAlchemy()
code_app = Flask("codesender.py")
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
server_db.init_app(code_app)


class User(server_db.Model):
    id = server_db.Column(server_db.Integer, primary_key=True)
    username = server_db.Column(server_db.String, unique=True, nullable=False)
    password = server_db.Column(server_db.String, unique=True, nullable=False)
    code_seg = server_db.Column(server_db.String)


class Admin(server_db.Model):
    id = server_db.Column(server_db.Integer, primary_key=True)
    admin_name = server_db.Column(server_db.String, unique=True, nullable=False)
    admin_pass = server_db.Column(server_db.String, unique=True, nullable=False)


with code_app.app_context():
    server_db.create_all()


@code_app.route("/users")
def user_list():
    code_app_users = server_db.session.execute(server_db.select(User).order_by(User.username)).scalars()
    return render_template("user/list.html", users=code_app_users)


@code_app.route("/users/create", methods=["GET", "POST"])
def user_create():
    if request.method == "POST":
        user = User(
            username=request.form["username"],
            password=request.form["password"],
        )
        server_db.session.add(user)
        server_db.session.commit()
        return redirect(url_for("user_detail", id=user.id))

    return render_template("user/create.html")


@code_app.route("/user/<int:id>")
def user_detail(usr_id):
    user = server_db.get_or_404(User, usr_id)
    return render_template("user/detail.html", user=user)


@code_app.route("/user/<int:id>/delete", methods=["GET", "POST"])
def user_delete(usr_id):
    user = server_db.get_or_404(User, usr_id)

    if request.method == "POST":
        server_db.session.delete(user)
        server_db.session.commit()
        return redirect(url_for("user_list"))

    return render_template("user/delete.html", user=user)


@code_app.route("/user/<int:id>/code_seg", methods=["GET", "POST"])
def add_code(user_id):
    if request.method == "POST":
        code_seg = User(
            username=request.form["username"],
            code=request.form["code"],
        )
        server_db.session.add(code_seg)
        server_db.session.commit()
        return redirect(url_for("user_detail", id=user_id))

    return render_template("user/<int:id>/code_seg.html")
