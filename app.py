import os
import re
from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory

app = Flask(__name__)
app.secret_key = 'your_secret_key'

users = {
    "user@example.com": "password123"
}

#check if email follows normal conventions
email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            return redirect(url_for('tickets'))
        else:
            flash('Invalid username or password')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/tickets')
def tickets():
    return render_template('tickets.html')

@app.route('/countdown')
def countdown():
    return render_template('countdown.html')

@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    if request.method == 'POST':
        email = request.form['email-address']
        username = request.form['new-username']
        password = request.form['new-password']
        retype_password = request.form['retype-password']

        # Validate email format
        if not re.match(email_regex, email):
            flash('Invalid email address')
            return redirect(url_for('create_account'))

        # Check if email or username already exists
        if email in users or username in users:
            flash('Email or username already exists')
            return redirect(url_for('create_account'))

        # Validate username
        if len(username) < 6:
            flash('Username must be at least 3 characters long')
            return redirect(url_for('create_account'))

        # Validate password
        if len(password) < 6:
            flash('Password must be at least 6 characters long')
            return redirect(url_for('create_account'))

        # Check if passwords match
        if password != retype_password:
            flash('Passwords do not match')
            return redirect(url_for('create_account'))

        # Add new user to the dictionary
        users[username] = password

        flash('Account created successfully')
        return redirect(url_for('login'))

    return render_template('create_account.html')

@app.route('/pictures/<path:filename>')
def pictures(filename):
    return send_from_directory(os.path.join(app.root_path, 'pictures'), filename)

if __name__ == '__main__':
    app.run(debug=True)