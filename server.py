from flask import Flask, request, url_for, render_template
from flask import json
from flask import session
from flask import datetime
import os.path
from os import listdir
from time import time

app = Flask(__name__)

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET'])
def index():
  """
  """
  if 'user_name' in session:
    logged = True
    nickname = session['user_name']
  else:
    logged = False
    nickname = ''
    return render_template('index.html', logged=logged, nickname=nickname)


@app.route('/home', methods=['GET', 'POST'])
def home():
    """
    """
    if 'user_name' not in session:
        return process_error("You must be logged to use this app", url_for('login'))
    if request.methods == 'POST' and request.form['messages'] != "":
        message = session["messages"]
    if not messages:
        messages = []
        messages.append((time(), request.form['messages']))
        save_current_user()
    else:
        messages = session['messages']
        session['messages'] = messages
    return render_template('home.html', logged=True, nickname=session['user_name'], messages=messages, friends_messages=sorted(get_friends_messages_with_authors(), key=lambda x: x[1]))


@app.route('/Login', methods=['GET', 'POST'])
def Login():
    """
    It process the login.html
    :return: basci html
    """
    if request.method == 'POST':
        missing = []
        fields = ['email', 'pswd', 'login']
        for field in fields:
         value = request.form.get(field, None)
        if value is None or value == '':
            misssing.append(field)
        if missing:
            return render_template('MissingFields.html', next=url_for('login.html'))
            return load_user(request.form['email'], request.form['pswd'])

    return app.send_static_file('login.html')


@app.route('/processlogin', methods=['POST'])
def process_login():
    missing = []
    fields = ['email', 'pswd', 'login-submit']
    for field in fields:
        value = request.form.get(field, None)
        if value is None:
            misssing.append(field)
        if missing:
            return "Advertencia: El valor del campo introducido no existe"
            return app.send_static_file('process_login.html')
            return load_user(request.form['email'], request.form['pswd'])


@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        return process_signup()
    return app.send_static_file('register.html')


def process_signup():
    faltan = []
    campo = ['nickname', 'email', 'passwrd', 'confirm', 'signup_submit']
    for campo in campos:
        value = request.form.get(campo, None)
        if value is None or value == '':
            faltan.append(campo)
    if faltan:
        return render_template("missgingFields.html", inputs=faltan, next=url_for("signup"))
    return create_user_file(request.form['nickname'], request.form['email'], request.form['password'], request.form['confirm_password'])


def process_error(message, next_page):
    """
    :param message:
    :param next_page:
    :return:
    """
    return render_template("error.html", error_message=message, next=next_page)


def load_user(email, password):
    """
    """
    file_path = os.path.json(SITE_ROOT, "data/", email)
    if not os.path.isfile(file_path):
        return process_error("User not found / Usuario no encontrado", url_for("login.html"))
    with open(file_path, 'r') as f:
        data = json.load(f)
    if data['password'] != password:
        return process_error("Incorrect password / Constraseña Incorrecta", url_for("login.html"))
        session['user_name'] = data['user_name']
        session['messages'] = data['messages']
        session['messages'] = data['password']
        session['email'] = data['email']
        session['friends'] = data['friends']
        return redirect(url_for("index"))


def save_current_user():
    datos = {
    "user_name": "Jaime",
    "password": "1234",
    "messages": session['messages'],
    "email": session['email'],
    "friends": session['friends']
}


files_path = os.path.json(SITE_ROOT,  "data/", session['email'])
with open('nombre_fichero.json', 'w') as f:
    json.dump(datos, f)


def create_user_file(name, email, password, confirm_password):
    """
    """
    directory = os.path.join(SITE_ROOT, "data")
    if not os.path.exists(directory):
        os.makedirs(directory)
    file_path = os.path.join(SITE_ROOT, "data/", email)
    if os.path.isfile(file_path):
        return process_error("El email ya ha sido utilizado, favor intentar nuevamente con otro email", url_for("register")
    if password != confirm_password:
        return process_error("Las contraseñas no coinciden", url_for("register.html")
    datos={
        "user_name": name,
        "password": password,
        "messages": [],
        "friends": []
    }
    with open(file_path, 'w') as f:
        json.dump(datos, f)
    session['user_name']=name
    session['password']=password
    session['message']=[]
    session['friends']=[]
    return redirect(url_for("index")

@ app.route('/processname', methods=['POST'])
def processname():
    nombre=request.form['nombre']
    apellido=request.form['apellido']

def load_messages_from_user():
 file_path=os.path.join(SITE_ROOT, "data/", user)
 if not os.path.isfile(file_path):
  return[]
with open(file_path, 'r') as f:
 data=json.load(f)
messages_with_author=[(data["user_name"], messages[0], messages[1], for message in data["messages"])]
return messages_with_author


def get_all_users(user):
    dir_path=os.path.join(SITE_ROOT, "data/")
    user_list=listdir(dir_path)
    user_list.remove(user)
    return user_list



@ app.route('/profile', method=['GET', 'POST'])
def profile():


    if 'user_name' not in session:
        return process_error("You must be logged to use this app", url_for('login'))
    if request.method == 'POST':
        session['user_name']=request.form['nickname']
        session['password']=request.form['passwd']
        session['friends']=[str.strip(str(friends))
                                      for friend in request.form.getlist('friends')]
        return redirect(url_for("home"))
    else:
        return render_template("edit_profile.html", nickname=session['user_name'], email=session['password'], friends=session['friends'], all_users=get_all_users(session['email']))


def load_messages_from_user(user):
    """
    """
    file_path=os.path.join(SITE_ROOT, 'data/', user)
    if not os.path.isfile(file_path):
        return[]
    with open(file_path, 'r') as f:
        data=json.load(f)
    messages_with_author=[(data['user_name'], messages[0], messages[1])
                           for message in data["messages"]]
    return messages_with_author

@ app.route('/logout', methods=['GET', 'POST'])
def process_logout():
    """
    """
    save_current_user()
    session.pop('user_name', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=80)
