from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login")
def logIn_SignIn():
    return render_template('login.html')


if __name__ == "__main__":
    app.run()
