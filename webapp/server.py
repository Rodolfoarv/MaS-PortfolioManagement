from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

import sys
sys.path.append('../')
from src.coordinator import Coordinator

import read_api
import os
import MySQLdb

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

@app.route("/validatelogin/", methods=['POST'])
def retrieve_user_credentials():
    form_data = request.form
    email = form_data['email']
    passwd = form_data['password']
    user = read_user_from_db(email, passwd)

    if (user):
        session['username'] = user
        return redirect("/index")
    
    print(user)
    return redirect("/login")

@app.route("/register/", methods=['POST'])
def get_user_registration():
    form_data = request.form
    #print(form_data['names'])
    passwd = form_data['password']
    confrm = form_data['confirm-password']

    if (validate_registration_password(passwd, confrm)):
        insert_user_into_db(form_data)
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

def read_user_from_db(email, passwd):
    db = MySQLdb.connect(host = '127.0.0.1',
                         user = 'root',
                         passwd = 'passcode',
                         db = 'PortafolioInversiones')
    cursor = db.cursor()

    try:
        cursor.execute("SELECT * FROM Usuario WHERE Correo = '%s'" % (email))
        rows = cursor.fetchall()
        for row in rows:
            if (row[5] == passwd):
                return row[1]
            else:
                continue
    except:
        print("Unable to fetch data.")

    cursor.close()
    db.close()
    return 0

def insert_user_into_db(data):
    email = data['email']
    names = data['names']
    lname1 = data['lname1']
    lname2 = data['lname2']
    datebirth = data['datebirth']
    password = data['password']
    budget = data['budget']

    db = MySQLdb.connect(host = '127.0.0.1',
                         user = 'root',
                         passwd = 'passcode',
                         db = 'PortafolioInversiones')
    cursor = db.cursor()

    try:
        cursor.execute("""INSERT INTO Usuario VALUES (%s,%s,%s,%s,%s,%s,%s)""",
                    (email, names, lname1, lname2, datebirth, password, budget))
        db.commit()
    except:
        print("Could not insert values to the database.")
        db.rollback()
    
    cursor.close()
    db.close()

if __name__ == "__main__":
    #app.run()
    app.run(port=1200)

app.secret_key = os.urandom(32)
print("Cleared secret key...")
