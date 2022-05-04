from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def render_homepage():
    return render_template("home.html")

@app.route('/people')
def render_people():
    return render_template("people.html")

@app.route('/definitions')
def render_definitions():
    return render_template("definitions.html")

@app.route('/ㅤㅤㅤㅤㅤ')
def render_ㅤㅤㅤㅤㅤ():
    return render_template("ㅤㅤㅤㅤㅤ.html")



app.run(host="0.0.0.0")