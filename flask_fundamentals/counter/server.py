from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():
    session['counter'] += 1
    return render_template('index.html')

@app.route('/counter', methods=['POST'])
def plus2():
    session['counter'] += 1
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['counter'] = 0
    return redirect('/')

app.run(debug=True)