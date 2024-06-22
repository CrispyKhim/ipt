from flask import Flask, render_template, redirect, url_for, request
import requests

app = Flask(__name__)

# Main Index Page
@app.route('/')
def index():
    return render_template('index.html')

# 404 Error page
@app.route('/<name>')
def error():
    return render_template('error.html')

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
        # Get image from API
        response = requests.get("https://api.thecatapi.com/v1/images/search?limit=1&random=RAND&api_key='live_ug7L3YzsrAvPthkUAcOVWqHTJfnd4b6u1NFao0EhLllQDwmokv9iEXeUgQOuoljn'").json()
        # Get the image from the result
        image_url = response[0]['url']
        width = response[0]['width'] * 0.9
        height = response[0]['height'] * 0.9
        return render_template('/users/Home.html', username=username, search_term=search_term, image_url=image_url, check=check, width=width, height=height)
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

# Connect Page
@app.route('/home/<string:username>/connect')
def connect(username):
    return render_template('/users/connect.html', username=username)

# Learn Page - After login
@app.route('/home/<string:username>/learn')
def Learn_user(username):
    return render_template('/users/learn.html', username=username)





if __name__ == '__main__':
    app.run(debug=True)