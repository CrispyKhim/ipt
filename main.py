from flask import Flask, render_template, redirect, url_for, request, jsonify
from cat_api import get_random_cat_image

app = Flask(__name__)
app.secret_key = 'supersecretkey'


global username
try:
    username = request.form.get('login-username') # Username saved
except:
    username = "" # Username saved

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

# legal Page
@app.route('/features')
def features():
    return render_template('features.html')

# legal Page
@app.route('/legal')
def legal():
    return render_template('legal.html')

# Contact Page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    feedback = False
    if request.method == 'POST':
        # Feedback saved
        feedback = True
        email = request.form.get('feedback-email') # Email saved
        comment = request.form.get('feedback-comment') # Comment saved
        return render_template('/contact.html', feedback=feedback)
    else:
        return render_template('/contact.html', feedback=feedback)


# Login / Register Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        global email, username, password
        email = request.form.get('login-email') # Email saved
        username = request.form.get('login-username') # Username saved
        password = request.form.get('login-password') # Password saved
        return redirect(url_for('home', username=username))
    else:
        return render_template('login.html')

# Home Page
@app.route('/redirectHome', methods=['GET', 'POST'])
def redirectHome():
    return redirect(url_for('home', username=username))

# Home Page
@app.route('/<string:username>/home', methods=['GET', 'POST'])
def home(username):
    return render_template('/users/Home.html', username=username)

# Home Page
@app.route('/home/random', methods=['GET', 'POST'])
def random():
    cat_image = get_random_cat_image()
    return render_template('/users/random.html', cat_image=cat_image)
        
# Browse Page
@app.route('/home/browse', methods=['GET', 'POST'])
def browse():
    check = False
    if request.method == 'POST':
        check = True
        search_term = request.form.get('search')
        return render_template('/users/browse.html', search_term=search_term, check=check)
    else:
        return render_template('/users/browse.html')

# Vocal Page
@app.route('/home/vocal', methods=['GET', 'POST'])
def vocal():
    return render_template('/users/vocal.html')

# Learn Page
@app.route('/home/learn')
def learn():
    return render_template('/users/learn.html')

# Cat API
@app.route('/random_cat')
def random_cat():
    cat_image = get_random_cat_image()
    if cat_image:
        return jsonify({'url': cat_image['url']})
    else:
        return jsonify({'error': 'Failed to load cat image'}), 500

if __name__ == '__main__':
    app.run(debug=True)