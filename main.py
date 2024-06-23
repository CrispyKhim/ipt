from flask import Flask, render_template, redirect, url_for, request
import requests


app = Flask(__name__)

# Main Index Page
@app.route('/')
def index():
    return render_template('index.html')

# 404 Error page
@app.route('/<string:name>')
def error(name):
    return render_template('error.html', name=name)

# About Page
@app.route('/about', methods=['GET', 'POST'])
def about():
    feedback = False
    if request.method == 'POST':
        # Feedback saved
        feedback = True
        email = request.form.get('feedback-email') # Email saved
        comment = request.form.get('feedback-comment') # Comment saved
        return render_template('about.html', feedback=feedback)
        
    else:
        return render_template('about.html', feedback=feedback)

# Learn Page
@app.route('/learn')
def learn():
    return render_template('learn.html')

# legal Page
@app.route('/features')
def features():
    return render_template('features.html')

# legal Page
@app.route('/legal')
def legal():
    return render_template('legal.html')


# Login / Register Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('login-email') # Email saved
        username = request.form.get('login-username') # Username saved
        password = request.form.get('login-password') # Password saved
        return redirect(url_for('home', username=username))
    else:
        return render_template('login.html')

# Home Page
@app.route('/home/<string:username>', methods=['GET', 'POST'])
def home(username):
    check = False
    if request.method == 'POST':
        check = True
        search_term = request.form.get('search')
        return render_template('/users/Home.html', username=username, search_term=search_term, check=check)
    else:
        return render_template('/users/Home.html', username=username, check=check)

# Favourites Page
@app.route('/home/<string:username>/favourites')
def favourites(username):
    return render_template('/users/favourites.html', username=username)

# Share Page
@app.route('/home/<string:username>/share')
def share(username):
    return render_template('/users/share.html', username=username)

# Browse Page
@app.route('/home/<string:username>/browse')
def browse(username):
    return render_template('/users/browse.html', username=username)

# Learn Page - After login
@app.route('/home/<string:username>/listen')
def listen(username):
    return render_template('/users/listen.html', username=username)


if __name__ == '__main__':
    app.run(debug=True)