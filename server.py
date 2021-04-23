from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods =['GET'])
def index():
  return app.send_static_file('index.html')

@app.route('/login',methods=['GET'])
def login():
    return app.send_static_file('login.html')

@app.route('/processLogin', methods=['POST'])
def process_login():
  missing = []
  fields = ['email', 'password', 'login_submit']

@app.route('/signup',methods=['GET'])
def signup():
    return app.send_static_file('register.html')

if __name__ == '__main__':
  app.run(debug = True, port = 80)