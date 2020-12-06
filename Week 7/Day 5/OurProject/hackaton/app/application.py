from flask import render_template, redirect, url_for,flash, request
from app import wtform_fields, db, app
from app.models import User
from flask_login import LoginManager, login_user, current_user,login_required,  logout_user


login =LoginManager(app)
login.init_app(app)


@login.user_loader
def load_user(id):
    return User.query.get(id)

@app.route("/", methods=['GET', 'POST'])
def index():
    reg_form = wtform_fields.RegistrationForm()
    if reg_form.validate_on_submit():

        username = reg_form.username.data
        password = reg_form.password.data

        """user_object = User.query.filter_by(username = username).first()
        if user_object:
            return "Username already taken" """

        hashed_pswd = pbkdf2_sha256.hash(password)

        user = User(username=username, password=hashed_pswd)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template("index.html", form=reg_form)


@app.route("/login", methods=['GET', 'POST'])
def login():

    login_form = wtform_fields.LoginForm()

    if login_form.validate_on_submit():
        user_object = User.query.filter_by(username=login_form.username.data).first()
        login_user(user_object)
        return redirect(url_for('chat'))

    return render_template("login.html", form=login_form)

@app.route("/chat", methods=['GET', 'POST'])
def chat():

    if not current_user.is_authenticated:
        return "Please, login before starting a conversation"

    return "chat with me"

@app.route("/logout", methods=['GET'])
def logout():
    logout_user()
    return "logout"