import sqlite3
from functools import wraps

from flask import Flask, flash, redirect, render_template,\
    request, session, url_for

# config
app = Flask(__name__)
app.config.from_object('_config')

# helper functions

# function used to connect to app configuration database
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def login_required(test):
    @wraps(test)
    def wrap(*args,**kwargs):
        if 'logged_in' in session:
            return test(*args,**kwargs)
        else:
            flash("You need to login first")
            return redirect(url_for('login'))
    return wrap


# route handlers
@app.route('/logout')
def logout():
    session.pop('logged_in',None)
    flash('Good bye...!')
    return redirect(url_for('login'))

@app.route('/', methods = ['GET','POST'])
def login():
    # return render_template('login.html')
    error = None
    status_code = 200
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] or \
            request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid Credentials. Please try Again'
            # status_code = 401
        else:
            session['logged_in'] = True
            flash("Login Successful...!")
            return redirect(url_for('tasks'))
    # return render_template('login.html', error = error), status_code
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)
