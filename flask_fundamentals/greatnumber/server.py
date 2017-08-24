from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'secretkey'

@app.route('/')
def index():
    import random
    if not session.has_key('randnumber'):
        session['randnumber'] = random.randrange(1,101)

    if not session.has_key('text'):
        session['text'] = ''

    if not session.has_key('color'):
        session['color'] = ''
    
    return render_template('index.html', text=session['text'], color=session['color'])

@app.route('/number', methods=['POST'])
def randomnumber():
    session['number'] = int(request.form['number'])

    if(session['number'] == session['randnumber']):
        session['text'] = str(session['randnumber']) + ' was the number!!'
        session['color'] = 'green'

    elif(session['number'] < session['randnumber']):
        session['text'] = 'Too low'
        session['color'] = 'red'

    elif(session['number'] > session['randnumber']):
        session['text'] = 'Too high'
        session['color'] = 'red'
    
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.pop('randnumber')
    session.pop('number')
    session['text'] = ''

    return redirect('/')
app.run(debug=True)