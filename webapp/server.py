from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

import sys
sys.path.append('../')
from src.coordinator import Coordinator

import read_api

app = Flask(__name__)
app.secret_key = "secret key"

"""
/*********************************************************************
 *                        Redirection Methods
 ********************************************************************/
"""

@app.route("/")
def home():
    return redirect("/login")

@app.route("/index")
def index():
    current_stocks = read_api.read_stocks()
    user = session['username']
#    coordinator = Coordinator("coordinator@"+"127.0.0.1","secret")
#    coordinator.start()
    return render_template('index.html',
                           stocks = current_stocks,
                           username = user)

@app.route("/login")
def logIn_SignIn():
    return render_template('login.html')

@app.route("/register/", methods=['POST'])
def get_user_registration():
    form_data = request.form
    #print(form_data['names'])
    passwd = form_data['password']
    confrm = form_data['confirm-password']

    if (validate_registration_password(passwd, confrm)):
        session['username'] = form_data['names']
        return redirect("/index")
    return redirect("/login")

@app.route("/q1", methods=["POST"])
def showAllStockData():
    data = request.data
    print data
    return render_template('login.html')

# @app.route("/q2", methods=["POST"])
# def showAllStockData():
#     data = request.data
#     print data
#     return render_template('login.html')

"""
/*********************************************************************
 *                          Auxiliary Methods
 ********************************************************************/
"""

def validate_registration_password(passwd, confirmation):
    return passwd == confirmation

if __name__ == "__main__":
    #app.run()
    app.run(port=1200)
