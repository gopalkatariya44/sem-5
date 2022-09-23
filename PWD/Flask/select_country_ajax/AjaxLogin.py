from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def load_login():
    return render_template("Login.html")


@app.route('/validate_login')
def validate_login():
    login_username = request.args.get('loginUsername')
    login_password = request.args.get('loginPassword')

    print("login_username>>>>>>>>", login_username)
    print("login_password>>>>>>>>", login_password)

    username = "admin"
    password = "admin"

    if login_username == username and login_password == password:
        response_message = "Welcome Admin !"
    else:
        response_message = "The username and password is incorrect !"

    return jsonify(response_message)


if __name__ == '__main__':
    app.run(threaded=True, port=5678)
