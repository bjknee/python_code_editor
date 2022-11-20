from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

"""
Author: Kayla Malcolm, CS 2005 G Team
Cycle Initiation: Cycle 6
This module serves a revision to the serverStorage module, by incorporating a database storage method as opposed to the
serverStorage module's use of Shelve. This is to provide a much more robust means of storing user profiles and 
codespaces, as well as a storage solution that can be scaled much more easily.
"""


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
server_db = SQLAlchemy(app)
# server_db.init_app(code_app)


class User(server_db.Model):
    id = server_db.Column(server_db.Integer, primary_key=True)
    username = server_db.Column(server_db.String, unique=True, nullable=False)
    password = server_db.Column(server_db.String, unique=True, nullable=False)
    code_seg = server_db.Column(server_db.String)


class Admin(server_db.Model):
    id = server_db.Column(server_db.Integer, primary_key=True)
    admin_name = server_db.Column(server_db.String, unique=True, nullable=False)
    admin_pass = server_db.Column(server_db.String, unique=True, nullable=False)


