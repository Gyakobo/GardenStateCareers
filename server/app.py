import uuid
from flask import Flask, request, render_template
from flask_smorest import abort
from db import stores, items
import os

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'templates')
# template_dir = os.path.join(template_dir, 'login_signup')
print(template_dir)

app = Flask(__name__, template_folder=template_dir)

#######################
# MAIN
#######################

# Main page 
@app.route("/")
def main_page():
    return render_template("main/html/main.html") 

# Login page 
@app.route("/login")
def home_page():
    return render_template("login_signup/html/login.html") 



