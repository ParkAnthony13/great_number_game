from flask import Flask, redirect, render_template, session, request
import random
app = Flask(__name__)
app.secret_key = 'speak friend and enter'

@app.route('/')
def home():
    if 'attempt' in session:
        print("not a new session")
    else:
        session['answer'] = random.randint(1,100)
        session['attempt'] = 0
        session['state'] = 0
        print(f"The number is: {session['answer']}")
    return render_template('index.html', answer = session['answer'])


@app.route('/attempt', methods=['POST'])
def guess():
    session['guess']=int(request.form['guess'])
    session['attempt'] += 1
    print(f"attempts: {session['attempt']}")
    if int(session['guess']) == session['answer']:
        print('correct')
        session['state'] = 1
        print(session['state'])
    else:
        print('wrong')
        if int(session['guess']) > session['answer']:
            session['state'] = 2
            print("too high")
        elif int(session['guess']) < session['answer']:
            session['state'] = 3
            print("too low")
    if session['attempt'] == 5:
        print("5 attempts made")
        session['state'] = 4
        session.clear()
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)