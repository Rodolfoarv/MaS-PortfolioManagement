from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

import sys
sys.path.append('../')
from src.coordinator import Coordinator

app = Flask(__name__)

@app.route("/")
def index():
    	coordinator = Coordinator("coordinator@"+"127.0.0.1","secret")
    	coordinator.start()
        return render_template('index.html')

@app.route("/login")
def logIn_SignIn():
    return render_template('login.html')

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

if __name__ == "__main__":
    app.run()
