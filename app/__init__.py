from flask import Flask, render_template
app = Flask(__name__,
	static_url_path='/static',
	static_folder='static')

@app.route('/')
def index():
	return render_template('heart.html')

@app.route('/login')
def login():
	return render_template('login.html')