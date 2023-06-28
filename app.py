from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello, World! How are you? I am fine.'

@app.route('/')
def index():
    return render_template('index.html')