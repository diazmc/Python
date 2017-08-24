from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

@app.route('/')
def index():
    return render_template ('index.html')

@app.route('/ninja')
def ninja():
    showall = True
    return render_template('ninjas.html', showall=showall)

@app.route('/ninja/<ninja_color>')
def getColor(ninja_color):
    showall = False
    return render_template('ninjas.html', color=ninja_color, all=showall)

app.run(debug=True)