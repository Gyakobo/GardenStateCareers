import uuid
from flask import Flask, request, render_template, jsonify
from flask_smorest import abort
from db import stores, items, users
import os

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'templates')
# template_dir = os.path.join(template_dir, 'login_signup')
print(template_dir)

# app = Flask(__name__, template_folder=template_dir)
app = Flask(__name__)

#######################
# MAIN PAGE
#######################

landing_user = ""

# Main page 
@app.route("/")
def main_page():
    return render_template("main/main.html") 

@app.route("/validate-user", methods=["POST"])
def validate_user():
    if request.method == "POST":
        user = request.get_json()["email"]
        if user not in users:
            return jsonify({"user_exist": "true"})
        else:
            return jsonify({"user_exist": "false"})

@app.route("/user_or_company", methods=["POST"])
def user_or_company():
    if request.method == 'POST':
        landing_user = request.form.get('email')

    print(landing_user)

    return render_template("login_signup/student_or_company.html") 

# Login page 
@app.route("/login_or_signup", methods=["POST"])
def login_page():
    if request.method == 'POST':
        if request.form.get('Student') == 'Student':
            return render_template("login_signup/login_student.html") 
        elif  request.form.get('Recruiter') == 'Recruiter':
            return render_template("login_signup/login_company.html") 
        else:
            return "Smth went wrong..."

@app.route("/register", methods=["POST"])
def user_register():
    if request.method == 'POST':
        pass
    return "So far so good"




