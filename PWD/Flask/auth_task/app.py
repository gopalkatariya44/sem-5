from flask import Flask, session, redirect, url_for, render_template, request

app = Flask(__name__)
app.secret_key = "hello"


@app.route('/')
def home():
    session.clear()
    return render_template('register.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    session.permanent = True
    session['firstname'] = request.form.get('firstname')
    session['lastname'] = request.form.get('lastname')
    session['username'] = request.form.get('username')
    session['password'] = request.form.get('password')
    return render_template('login.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/login-validate', methods=['POST'])
def login_validate():
    if (session['username'] == request.form.get('username')) and (
            session['password'] == request.form.get('password')):
        return render_template('welcome.html')
    else:
        return redirect(url_for('login'))


@app.route('/welcome')
def welcome():
    name = session['firstname'] + ' ' + session['lastname']
    print(session['firstname'])
    return render_template('welcome.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
