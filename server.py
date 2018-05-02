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
@app.route("/users")
def display_info():
    

    return render_template("one_user.html")
app.run(debug=True)
