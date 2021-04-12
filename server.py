from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods="['GET']")
def index():
  return app.send_static_file('index.html')

@app.route('/login',methods="['GET']")
def login():
    return app.send_static_file('login.html')

@app.route('/signup',methods="['GET']")
def signup():
    return app.send_static_file('register.html')