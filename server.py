from flask import Flask, request, redirect, render_template, session, flash,url_for
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
mysql = MySQLConnector(app,'users')
@app.route("/")
def index():
    display_query = "SELECT * FROM users"
    users = mysql.query_db(display_query)
    return render_template("index.html", all_users = users)
@app.route("/users/<id>")
def display_info(id):
    person = users.query.filter_by(id = id).first()
    return render_template("one_user.html", all_person = person)
app.run(debug=True)
