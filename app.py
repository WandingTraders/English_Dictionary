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
    except Exception as error:
        print(error)
        return None

@app.route('/')
def render_homepage():
    return render_template("home.html")

@app.route('/definitions')
def render_definitions():

    #use connect function
    conn = create_connection(database)
    #write the query
    query = "SELECT * FROM 'English_Words';"
    # query = "SELECT * FROM 'English_Words' WHERE word_type = 'Animals';"
    cursor = conn.execute(query)
    results = cursor.fetchall()
    print(cursor.fetchall())
    conn.close()

    return render_template("definitions.html", results=results)

@app.route('/people')
def render_people():
    return render_template("people.html")

@app.route('/login')
def render_login():
    return render_template("login.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

@app.route('/ㅤㅤㅤㅤㅤ')
def render_ㅤㅤㅤㅤㅤ():
    return render_template("ㅤㅤㅤㅤㅤ.html")



app.run(host="0.0.0.0")