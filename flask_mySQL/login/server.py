from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

import os, binascii
salt = binascii.b2a_hex(os.urandom(15))

app = Flask(__name__)
mysql = MySQLConnector(app,'logindb')
app.secret_key = 'secret'

@app.route('/')
def index():
    return render_template('index.html')

import md5
@app.route('/process', methods=['POST'])
def register():
    if len(request.form['first_name']) < 2:
        flash("Need at least 2 characters")
        return redirect('/')

    elif len(request.form['last_name']) < 2:
        flash("Need at least 2 characters")
        return redirect('/')

    elif not EMAIL_REGEX.match(request.form['email_address']):
        flash("Invalid Email Address!")
        return redirect('/')
    
    elif len(request.form['password']) < 8:
        flash("Password needs at least 8 characters")
        return redirect('/')

    elif request.form['password'] != request.form['con_password']:
        flash("Needs to match password!!")
        return redirect('/')

    else:
        password = request.form['password']
        salt =  binascii.b2a_hex(os.urandom(15))
        hashed_pw = md5.new(password + salt).hexdigest()

        query = "INSERT INTO usertable (first_name, last_name, email_address, password, salt) VALUES (:first_name, :last_name, :email_address, :password, :salt)"
        data = {
                'first_name': request.form['first_name'],
                'last_name': request.form['last_name'],
                'email_address': request.form['email_address'],
                'password': hashed_pw,
                'salt': salt
                }
        mysql.query_db(query,data)

        session['first_name'] = request.form['first_name']
        session['last_name'] = request.form['last_name']
        session['email_address'] = request.form['email_address']
        session['password'] = request.form['password']
        
    return redirect('/loggedin')

@app.route('/loggedin')
def hi():
    return render_template('success.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/processlogin', methods=['POST'])
def process():
    
    if len(request.form['login_email']) < 1:
        flash("Email cannot be blank")
        return redirect('/login')

    elif len(request.form['login_password']) < 1:
        flash("Need password")
        return redirect('/login')

    elif not EMAIL_REGEX.match(request.form['login_email']):
        flash("Invalid Email Address!")
        return redirect('/login')

    else:
        password = md5.new(request.form['login_password']).hexdigest()
        email = request.form['login_email']
        user_query = "SELECT * FROM usertable where usertable.email_address = :email_address AND usertable.password = :password"
        query_data = { 'email_address': email, 'password': password}
        user = mysql.query_db(user_query, query_data)
        
        return redirect('/loggedin')
    


app.run(debug=True)