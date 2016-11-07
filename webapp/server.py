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

""" Home Access """
@app.route("/")
def home():
    return redirect("/login")

"""
/*********************************************************************
 *                       Index and Main Methods
 ********************************************************************/
"""

""" Index Dashboard Page """
@app.route("/index")
def index():
    current_stocks = read_api.read_stocks()
    user = session['username']
#    coordinator = Coordinator("coordinator@"+"127.0.0.1","secret")
#    coordinator.start()
    return render_template('index.html',
                            stocks = current_stocks,
                            username = user)

""" Logout Action """
@app.route("/logout")
def logout():
    session['username'] = None
    session['email'] = None
    return redirect("/")

"""
/*********************************************************************
 *                        Login and Register
 ********************************************************************/
"""

""" Login Page """
@app.route("/login")
def logIn_SignIn():
    return render_template('login.html')

""" Login POST Action """
@app.route("/validatelogin/", methods=['POST'])
def retrieve_user_credentials():
    form_data = request.form
    email = form_data['email']
    passwd = form_data['password']
    user = read_user_from_db(email, passwd)

    if (user):
        session['username'] = user
        session['email'] = email
        return redirect("/index")
    
    print(user)
    return redirect("/login")

""" Register POST Action """
@app.route("/register/", methods=['POST'])
def get_user_registration():
    form_data = request.form
    #print(form_data['names'])
    passwd = form_data['password']
    confrm = form_data['confirm-password']

    if (validate_registration_password(passwd, confrm)):
        insert_user_into_db(form_data)
        session['username'] = form_data['names']
        session['email'] = form_data['email']
        return redirect("/index")

    return redirect("/login")

"""
/*********************************************************************
 *                             Profile
 ********************************************************************/
"""

""" Shares Page """
@app.route("/shares")
def shares():
    investing = read_spins_and_enterprises()
    spins = investing[0]
    enterprises = investing[1]

    preferences = read_user_prefs(session['email'])
    spin_data = preferences[0]
    entrp_data = preferences[1]

    # print(spins)
    # print(enterprises)

    return render_template('shares.html',
                            username = session['username'],
                            all_spns = spins,
                            all_entrps = enterprises,
                            usr_spns = spin_data,
                            usr_entrps = entrp_data)

""" Queries Page """
@app.route("/queries")
def queries():
    investing = read_spins_and_enterprises()
    spins = investing[0]
    enterprises = investing[1]

    preferences = read_user_prefs(session['email'])
    spin_data = preferences[0]
    entrp_data = preferences[1]

    # print(spins)
    # print(enterprises)

    return render_template('queries.html',
                            username = session['username'],
                            all_spns = spins,
                            all_entrps = enterprises,
                            usr_spns = spin_data,
                            usr_entrps = entrp_data)

""" Table Page """
@app.route("/table")
def table():
    investing = read_spins_and_enterprises()
    spins = investing[0]
    enterprises = investing[1]

    preferences = read_user_prefs(session['email'])
    spin_data = preferences[0]
    entrp_data = preferences[1]

    # print(spins)
    # print(enterprises)

    return render_template('table.html',
                            username = session['username'],
                            all_spns = spins,
                            all_entrps = enterprises,
                            usr_spns = spin_data,
                            usr_entrps = entrp_data)

"""
/*********************************************************************
 *                          Other Methods
 ********************************************************************/
"""

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

""" Validate the given password is correct when a user registers. """
def validate_registration_password(passwd, confirmation):
    return passwd == confirmation

""" Read a user's login credentials from the database. """
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

""" Insert a new entry with a new user's basic information to the database. """
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

""" Read a given user's investing preferences. """
def read_user_prefs(user_email):
    db = MySQLdb.connect(host = '127.0.0.1',
                         user = 'root',
                         passwd = 'passcode',
                         db = 'PortafolioInversiones')
    cursor = db.cursor()

    try:
        cursor.execute("SELECT * FROM PreferenciaGiro WHERE Correo = '%s'"
                        % (user_email))
        spins = cursor.fetchall()
        cursor.execute("SELECT * FROM PreferenciaEmpresa WHERE Correo = '%s'"
                        % (user_email))
        enterprises = cursor.fetchall()
        return [spins, enterprises]

    except:
        print("Unable to fetch user preferences.")
    
    cursor.close()
    db.close()
    return [0,0]

""" Read current possible spins and enterprises to invest. """
def read_spins_and_enterprises():
    db = MySQLdb.connect(host = '127.0.0.1',
                         user = 'root',
                         passwd = 'passcode',
                         db = 'PortafolioInversiones')
    cursor = db.cursor()

    try:
        cursor.execute("SELECT * FROM Giro")
        spins = cursor.fetchall()
        cursor.execute("SELECT * FROM Empresa")
        enterprises = cursor.fetchall()
    except:
        print("Could not retrieve spins and enterprises.")

    return [spins, enterprises]

if __name__ == "__main__":
    #app.run()
    app.run(port=1200)

app.secret_key = os.urandom(32)
print("Cleared secret key...")
