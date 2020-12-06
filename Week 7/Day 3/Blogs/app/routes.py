# First, we are in a different file, so we need to import the app
import flask
import os
from app import app    # app.app is package_name.variable_name
from flask import flash, render_template, abort
import flask_wtf
import wtforms
import flask_sqlalchemy
import flask_migrate
from datetime import datetime

app.config['SECRET_KEY'] = 'you-will-never-guess'
basedir = os.path.abspath(os.path.dirname(__file__)) # Try to avoid hardcoding paths, use os
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'app.db')
db = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)

class MyModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(50))
    price = db.Column(db.Float)
    dateNow = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return "Name:{} , Description: {}, Price: {}".format(name,description,price)

class Form(flask_wtf.FlaskForm):
    username = wtforms.StringField("Name")
    password = wtforms.PasswordField("Password")
    bio = wtforms.StringField("Bio")
    submit = wtforms.SubmitField("Submit")


@app.route("/",methods=("GET", "POST"))
def index():
    form = Form()
    if form.validate_on_submit():
        us = form.username.data
        pwd = form.password.data
        bio = form.bio.data
        msg = ("username: {}\n Password: {}\n bio: {}".format(us,pwd,bio))
    posts = [
        {"author":"John", "body":"I love python"},
        {"author":"Fish", "body":"I love water"},
        {"author":"Herpetolog", "body":"I love pythons"},
    ]

    return flask.render_template('index.html' , posts=posts, form=form)

@app.route("/home")
def home():
    flash("This is a flashed message.")
    flash("Successfully connected", "success")
    flash("There is an error.","danger")
    return render_template("home.html")

@app.route("/article")
def article():
    item1 = MyModel(name="Jeff", description="This is great", price=500)
    #article = ("Nike","This is better than Addidas",500)
    db.session.add(item1)
    db.session.commit()
    return render_template("article.html", item1=item1)


@app.errorhandler(404)
def error_404(error):
    #abort(404)
    return flask.render_template('404_error.html'), 404