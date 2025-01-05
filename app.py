from flask import Flask,render_template,request,redirect,session
from db import *
import api

dbo = Database()

app = Flask(__name__)
app.secret_key = b'\x12\xae\xe5\xb4x\xe7\xc2\xfb\xe6\xd3\x11\x94\xdaH\xd0\x13\x8a\xc1\xf9g\x93t'

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/perform_register',methods=['post'])
def perform_register():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    response = dbo.insert(name,email,password)
    if response == 1:
        return render_template('login.html',message='Registration Successful...Login to proceed')
    else:
        return render_template('login.html',message='Email already exists..Try Login In')

@app.route('/perform_login',methods=['post'])
def perform_login():
    
    email = request.form.get('email')
    password = request.form.get('password')

    response = dbo.search(email,password)
    if response == 1:
        session['logged_in'] = 1
        return redirect(f'/profile?email={email}')
    else:
        return render_template('login.html',message = 'Incorrect username or password...Try again !')

@app.route('/profile')
def profile():
    if 'logged_in' in session and session['logged_in'] == 1:
        email = request.args.get('email')
        return render_template('profile.html',message=dbo.db_return_name(email))
    else:
        return redirect('/')

@app.route('/ner')
def ner():
    if 'logged_in' in session and session['logged_in'] == 1:
        return render_template('ner.html')
    else:
        return redirect('/')

@app.route('/perform_ner',methods=['post'])
def perform_ner():
    if 'logged_in' in session and session['logged_in'] == 1:
        text = request.form.get('prompt')
        search = request.form.get('search')
        response = api.ner(text,search)
        print(response)
        return render_template('ner.html',response = response)
    else:
        return redirect('/')
    
@app.route('/sentiment_analysis')
def sentiment_analysis():
    if 'logged_in' in session and session['logged_in'] == 1:
        return render_template('sentiment_analysis.html')
    else:
        return redirect('/')
    
@app.route('perform_sentiment_analysis',methods=['post'])
def perform_sentiment_analysis():
    if 'logged_in' in session and session['logged_in'] == 1:
        text = request.form.get('prompt')
        response = api.sentiment_analysis(text)
        print(response)
        return render_template('sentiment_analysis.html',response=response)
    else:
        return redirect('/')

@app.route('/language_detection')
def abuse_detection():
    if 'logged_in' in session and session['logged_in'] == 1:
        return render_template('language_detection.html')
    else:
        return redirect('/')
    
@app.route('perform_language_detection',methods=['post'])
def perform_abuse_detection():
    if 'logged_in' in session and session['logged_in'] == 1:
        text = request.form.get('prompt')
        response = api.abuse_detection(text)
        print(response)
        return render_template('language_detection.html',response=response)
    else:
        return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

app.run(debug=True)