from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

import sys
sys.path.append('../')
from src.coordinator import Coordinator

import read_api

app = Flask(__name__)

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
#    coordinator = Coordinator("coordinator@"+"127.0.0.1","secret")
#    coordinator.start()
    return render_template('index.html',
                           stocks = current_stocks)

@app.route("/login")
def logIn_SignIn():
    return render_template('login.html')

@app.route("/register/", methods=['POST'])
def get_user_registration():
    form_data = request.form
    print(form_data['names'])
    return render_template('signup_success_test.html')

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

if __name__ == "__main__":
    #app.run()
    app.run(port=1200)
