import uuid
from subprocess import Popen, PIPE 
import subprocess 
from flask import Flask, request, render_template, jsonify
from flask_smorest import abort
from db import stores, items, students, student, recruiter, recruiters
from leetcode import leetcode
import os
import sys
import tempfile
from io import StringIO
import contextlib

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

def execute_cpp(cpp_code):
    # Get the C++ code from the request JSON data
    #data = request.get_json()
    #cpp_code = data.get('code', '')

    #if not cpp_code:
    #    return jsonify({"error": "No C++ code provided"})

    try:
        # Create a temporary directory and C++ source file
        with tempfile.TemporaryDirectory() as temp_dir:
            cpp_file_path = os.path.join(temp_dir, "user_code.cpp")
            exe_file_path = os.path.join(temp_dir, "user_code")

            # Write the C++ code to the source file
            with open(cpp_file_path, 'w') as cpp_file:
                cpp_file.write(cpp_code)

            # Compile the C++ code
            compile_command = f"g++ -o {exe_file_path} {cpp_file_path}"
            compile_result = subprocess.run(compile_command, shell=True, text=True, stderr=subprocess.PIPE)

            if compile_result.returncode != 0:
                return jsonify({"error": compile_result.stderr})

            # Execute the compiled code
            execution_result = subprocess.run(exe_file_path, shell=True, text=True, stdout=subprocess.PIPE)

            return jsonify({"output": execution_result.stdout})

    except Exception as e:
        return jsonify({"error": str(e)})

def execute_python(python_code :str):
    # Get the Python code from the request JSON data
    # data = request.get_json()
    # python_code = data.get('code', '')

    try:
        # Create a dictionary to hold the output
        exec_globals = {}
        exec_locals = {}
        exec(python_code, exec_globals, exec_locals)

        # Return the result as JSON
        return jsonify({"output_local": exec_locals})

    except Exception as e:
        # Handle errors if the Python code execution fails
        return jsonify({"error": str(e)})

def execute_command(command : str):
    # Specify the command you want to execute

    try:
        # Run the command and capture the output
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)

        # Create a dictionary to hold the command output
        output_dict = {
            "command": command,
            "output": result.stdout
        }
        # Return the output as JSON
        return jsonify(output_dict)

    except subprocess.CalledProcessError as e:
        # Handle errors if the command fails
        return jsonify({"error": str(e)})


# Main page 
@app.route("/")
def main_page():
    return render_template("main/main.html") 

@app.route("/run_leetcode_question", methods=["POST"])
def run_leetcode_question():
    if request.method == "POST":
        code = request.form.get('code')
        return execute_cpp(code)
        # return execute_command(code)
        # return execute_python(code)
        # return jsonify({exec(code)})

@app.route("/get_leetcode_question", methods=["POST"])
def get_leetcode_question():
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



