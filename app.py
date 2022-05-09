from flask import Flask
from flask import render_template
import table
import sqlite3

app = Flask(__name__)

database = "English_Dictionary.db"
def create_connection(db_file):
    try:
        connection = sqlite3.connect(db_file)
        connection.execute('pragma foreign_keys=ON')
        return connection
    except Error as error:
        print(error)
        return None

@app.route('/')
def render_homepage():
    return render_template("home.html")

@app.route('/definitions')
def render_definitions():

    #use connect function

    #write the query
    query = "SELECT * FROM 'Enlgish_Words' WHERE word_type = 'blah';"

    #make cursor object
    #use cursor obj to execute the function on the database.
    # save results
    # display results

    return render_template("definitions.html", data=table.returnTable())

@app.route('/people')
def render_people():
    return render_template("people.html")

@app.route('/login')
def render_login():
    return render_template("login.html")

@app.route('/ㅤㅤㅤㅤㅤ')
def render_ㅤㅤㅤㅤㅤ():
    return render_template("ㅤㅤㅤㅤㅤ.html")



app.run(host="0.0.0.0")