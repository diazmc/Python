from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friends')

@app.route('/')
def index():
    query = "SELECT * FROM friendstable"
    friendstable = mysql.query_db(query)
    return render_template('index.html', all_friends=friendstable)

@app.route('/friends', methods=['POST'])
def addFriend():
    query = "INSERT INTO friendstable(name, age, friends_since) VALUES (:name, :age, NOW())"

    data = {
            'name': request.form['name'],
            'age': request.form['age']
            }

    mysql.query_db(query, data)
    return redirect('/')


app.run(debug=True)