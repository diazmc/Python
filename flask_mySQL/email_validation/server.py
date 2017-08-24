from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import MySQLConnector

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
mysql = MySQLConnector(app,'email')
app.secret_key = 'secret'
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/insert', methods=['POST'])
def create():

    if len(request.form['email_address']) < 1:
        flash("Email cannot be blank!")
        return redirect('/')   
    
    elif not EMAIL_REGEX.match(request.form['email_address']):
        flash("Invalid Email Address!")
        return redirect('/')

    else:
        query = "INSERT INTO email_table(email_address, created_at, updated_at) VALUES(:email_address, NOW(), NOW())"
        data = {
                'email_address': request.form['email_address']
                }
        mysql.query_db(query, data)
        flash("Valid email address!!" + request.form['email_address'])

    return redirect('/success')

@app.route('/success')
def show():
    query = "SELECT * FROM email_table"
    email_table = mysql.query_db(query)

    return render_template('success.html', all_email=email_table)

app.run(debug=True)