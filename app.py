from flask import Flask, flash, redirect, render_template, session, abort

import os

app = Flask(__name__)

@app.route('/')
def home():
	if not session.get('logged_in'):
		return render_template('loggin.html')
	else:
		return "Hello Boss"

@app.route('/loggin', methods = ['POST'])
def admin_loggin():
	if request.form['password'] == 'password'and request.form['username'] == 'admin':
		session['logged_in'] = True
	else:
		flash('Wrong password')
	return home()
if __name__ =="__main":
	app.secret_key = os.urandom(12)
	app.run(debug=True, host='0.0.0.0', port=4000)



