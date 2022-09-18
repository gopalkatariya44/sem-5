from black import main
from flask import Flask, request, render_template, redirect

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/add_data', methods=['POST'])
def add_data():
    username = request.form.get('username')
    password = request.form.get('password')
    return render_template('view.html', username=username, password=password)


if __name__ == '__main__':
    app.run(debug=True)
