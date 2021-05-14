from flask import Flask, request, url_for

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    return app.send_static_file('index.html')


@app.route('/Login', methods=['GET', 'POST'])
def Login():
    if request.method == 'POST':
        missing = []
        fields = ['email', 'pswd', 'login']
        for field in fields:
         value = request.form.get(field, None)
        if value is None:
            misssing.append(field)
        if missing:
            return render_template('MissingFields.html',next = url_for('Login.html'))
            return load_user(request.form['email'], request.form['pswd'])

    return app.send_static_file('Login.html')


@app.route('/processlogin', methods=['POST'])
def process_login():
    missing = []
    fields = ['email', 'pswd', 'login']
    for field in fields:
        value = request.form.get(field, None)
        if value is None:
            misssing.append(field)
        if missing:
            return "Advertencia: El valor del campo introducido no existe"
            return app.send_static_file('process_login.html')
            return load_user(request.form['email'], request.form['pswd'])


@app.route('/registro', methods=['GET','POST'])

def registro(): 
    return app.send_static_file('registro.html')


#Fin de rutas

if __name__ == '__main__':  
    app.run(debug = True, port = 80)