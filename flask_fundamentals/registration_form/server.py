from flask import Flask, render_template, session, request, redirect, flash

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'secretkey'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def validate():
    email = request.form['email']
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    password = request.form['password']
    conpassword = request.form['conpassword']

    if len(email) < 1 or len(firstname) < 1 or len(lastname) < 1 or len(password) < 1 or len(conpassword) < 1:
        flash("All the form fields are required.")
        return redirect('/')
    
    elif password != conpassword:
        flash("Passwords have to match")
        return redirect('/')

    elif not EMAIL_REGEX.match(email):
        flash("Invalid email address!")
        return redirect('/')

    elif len(password) < 8:
        flash("Password should be more than 8 characters")
        return redirect('/')

    elif not re.match(r"[a-zA-Z]", firstname) or not re.match(r"[a-zA-Z]", lastname):
        flash("No numbers!!")
        return redirect('/')

    else:
        flash("Thanks for submitting your information.")


    return redirect('/')
    
app.run(debug=True)