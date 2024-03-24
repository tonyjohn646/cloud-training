from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user data
users = {
    "john": "password123",
    "alice": "abc123",
    "bob": "qwerty"
}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        return redirect(url_for('success', username=username))
    else:
        return render_template('login.html', message='Invalid username or password')

@app.route('/success/<username>')
def success(username):
    return f'Welcome, {username}!'

if __name__ == '__main__':
    app.run(debug=True)
