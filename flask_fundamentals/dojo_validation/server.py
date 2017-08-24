from flask import Flask, render_template, request, redirect, flash, session

app = Flask(__name__)
app.secret_key = 'secretkey'

@app.route('/')
def index():
    return render_template ('index.html')
    

@app.route('/result', methods=['POST'])
def submitInfo():
    
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comments = request.form['comments']
    
    if len(request.form['name']) < 1:
        flash("Name cannot be empty!!!")
        return redirect('/')
    else:
        flash("")
        
    if len(request.form['comments']) < 1:
        flash("Comments cannot be empty!!!")
        return redirect('/')
    elif len(request.form['name']) > 120:
        flash("Too long!!")
        return redirect('/')
    else:
        flash("")


    return render_template('info.html', name = name, location = location, language = language, comments = comments)

app.run(debug=True)