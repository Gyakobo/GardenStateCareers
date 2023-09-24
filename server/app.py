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

user = ""

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
            # users.append(email_address)

@app.route("/user_or_company", methods=["POST"])
def user_or_company():
    return render_template("login_signup/student_or_company.html") 

# Login page 
@app.route("/login_or_signup", methods=["POST"])
def login_page():
    if request.method == 'POST':
        if request.form.get('Student') == 'Student':
            # pass
            print("Student")
        elif  request.form.get('Recruiter') == 'Recruiter':
            # pass # do something else
            print("Recruiter")
        else:
            print("None")

    return render_template("login_signup/login.html") 



