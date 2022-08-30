from flask import Flask, render_template, redirect, url_for
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt

app = Flask(__name__)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'gopal'


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)


class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={'Placeholder': 'Username'})
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={'Placeholder': 'Password'})
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={'Placeholder': 'Username'})
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={'Placeholder': 'Password'})
    submit = SubmitField("Login")

    @staticmethod
    def validate_username(username):
        existing_username = User.query.filter.by(username=username.data).first()
        if existing_username:
            raise ValidationError('That user already exists.')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
