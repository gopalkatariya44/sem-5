from flask import Flask, session, render_template, request, flash, redirect, url_for
import pymysql

app = Flask(__name__)
app.secret_key = '''zjuhb4j3b45GFDSG$T$%^VWEDffbvwkwr#$%$fqeifjJVBVGJVTTFYer34534%BGE$%^3843tv34534BG$
%Tw4iu5697w45tw5f%ST%$65ej4g56iv4bk4jhw46H@^%hw469824hn6h456 '''


@app.route('/', methods=['POST', 'GET'])
def home():  # put application's code here
    session.clear()
    return render_template('register.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    session.permanent = True
    session['firstname'] = request.form.get('firstname')
    session['lastname'] = request.form.get('lastname')
    session['username'] = request.form.get('username')
    session['password'] = request.form.get('password')
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='12345678',
        db='gopal'
    )
    cursor = connection.cursor()
    try:
        query = "INSERT INTO user VALUES ({},{},{},{})".format(request.form.get('firstname'),
                                                               request.form.get('lastname'),
                                                               request.form.get('username'),
                                                               request.form.get('password'))
        cursor.execute(query)
        connection.commit()
    finally:
        cursor.close()
        connection.close()
    return render_template('login.html')
    # return render_template('result.html',result=user)


@app.route('/login', methods=['POST', 'GET'])
def login():
    session.permanent = True
    username = request.form.get('username')
    password = request.form.get('password')
    session_username = session['username']
    session_password = session['password']

    if username == "" and password == "":
        session.permanent = True
        flash("field can't be empty")
        return redirect(url_for('register'))

    elif (password == session_password) and (username == session_username):
        session.permanent = True
        flash("Succesfull Login")
        return redirect(url_for('welcome'))

    elif username != session_username and password == session_password:
        session.permanent = True
        flash("wrong email")
        return redirect(url_for('register'))
        # return render_template("welcome.html")
    elif password != session_password and username == session_username:
        session.permanent = True
        flash("wrong password")
        return redirect(url_for('register'))

    else:
        session.permanent = True
        flash("wrong email and password")
        # redirect and redirect url_for() and dont use render template
        return redirect(url_for('register'))


@app.route('/welcome', methods=['POST', 'GET'])
def welcome():
    return render_template('welcome.html')


@app.route('/logout')
def logout():
    session.pop("uname", None)
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
