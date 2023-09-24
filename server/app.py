import uuid
from flask import Flask, request, render_template, jsonify
from flask_smorest import abort
from db import stores, items, students, student, recruiter, recruiters
from leetcode import leetcode
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
client_type = ""

# Main page 
@app.route("/")
def main_page():
    return render_template("main/main.html") 

@app.route("/get_leetcode_question", methods=["POST"])
def get_leetcode_question():
    print("Entered")
    if request.method == "POST":
        leet_name = request.get_json()["leetcode"]
        print(leetcode[leet_name])
        return jsonify({"leetcode": leetcode[leet_name]})

@app.route("/validate-user", methods=["POST"])
def validate_user():
    if request.method == "POST":
        email = request.get_json()["email"]
        if email not in students or email not in recruiters:
            return jsonify({"user_exist": "true"})
        else:
            return jsonify({"user_exist": "false"})

@app.route("/user_or_company", methods=["POST"])
def user_or_company():
    global landing_user

    if request.method == 'POST':
        landing_user = request.form.get('email')
        if landing_user in students or landing_user in recruiters:
            return render_template("profile_page/profile_page.html")
        else:
            return render_template("login_signup/student_or_company.html") 


# Login page 
@app.route("/login_or_signup", methods=["POST"])
def login_page():
    global client_type
    if request.method == 'POST':
        if request.form.get('Student') == 'Student':
            client_type = "student"
            return render_template("login_signup/login_student.html") 
        elif  request.form.get('Recruiter') == 'Recruiter':
            client_type = "recruiter"
            return render_template("login_signup/login_company.html") 
        else:
            return "Smth went wrong..."

@app.route("/register_user", methods=["POST"])
def user_register():
    global client_type
    
    if request.method == 'POST':
        form = request.form
        if client_type == "student":
            student["first_name"] = request.form.get('firstname')
            student["last_name"] = form.get('lastname')
            student["gender"] = form.get('gender')
            student["location"] = form.get('location')
            student["university"] = form.get('university')
            student["major"] = form.get('major')
            student["start_date"] = form.get('start_date')
            student["end_date"] = form.get('end_date')
            student["email"] = form.get('email')
            student["phone"] = form.get('phone_number')
            students[student["email"]] = student
            
        elif client_type == "recruiter": 
            recruiter["first_name"] = request.form.get('firstname')
            recruiter["last_name"] = request.form.get('lastname')
            recruiter["company_name"] = request.form.get('Company_Name')
            recruiter["gender"] = request.form.get('gender')
            recruiter["location"] = request.form.get('location')
            recruiter["email"] = request.form.get('email')
            recruiter["phone"] = request.form.get('phone')
            recruiters[recruiter["email"]] = recruiter 

        print(students)
        print(recruiters)

    return render_template("profile_page/profile_page.html")



