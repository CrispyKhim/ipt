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
@app.route('/about')
def about():
    return render_template('about.html')


# Login / Register Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email') # Email saved
        username = request.form.get('username') # Username saved
        password = request.form.get('password') # Password saved
        return redirect(url_for('home', username=username))
    else:
        return render_template('login.html')

# Home Page
@app.route('/home/<string:username>', methods=['GET', 'POST'])
def home(username):
    if request.method == 'POST':
        search_term = request.form.get('search')
        check = True
        return redirect(url_for('search', username=username, search_term=search_term))
    else:
        return render_template('/users/Home.html', username=username)

# Rendering the searched result from user input
@app.route('/home/<string:username>/search-<string:search_term>', methods=['GET', 'POST'])
def search(username, search_term):
    # Get image from API
    response = requests.get("https://api.thecatapi.com/v1/images/search?limit=1&random=RAND&api_key='live_ug7L3YzsrAvPthkUAcOVWqHTJfnd4b6u1NFao0EhLllQDwmokv9iEXeUgQOuoljn'").json()
    # Get the image from the result
    image_url = response[0]['url']
    return render_template('/users/search.html', username=username, search_term=search_term, image_url=image_url)


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

# Learn Page
@app.route('/home/<string:username>/learn')
def learn(username):
    return render_template('/users/learn.html', username=username)





if __name__ == '__main__':
    app.run(debug=True)