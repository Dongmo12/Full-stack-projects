# First, we are in a different file, so we need to import the app
import flask
from flask import render_template, url_for, Flask
from app import app    # app.app is package_name.variable_name
# from app.form import Usercredentials
# import requests
import flask_login

users = []
# url = "https://amazon-products1.p.rapidapi.com/product"
#
# querystring = {"country":"US","asin":"B07CVL2D2S"}
#
# headers = {
#     'x-rapidapi-key': "a211f5681fmsh0a790654f9f52ebp125784jsn25cfd8b26524",
#     'x-rapidapi-host': "amazon-products1.p.rapidapi.com"
#     }
#
# response = requests.request("GET", url, headers=headers, params=querystring)




@app.route("/login",methods=("GET", "POST"))
def index():
    # form = Usercredentials()
    # if form.validate_on_submit():
    #     us = Usercredentials.username.data
    #     pwd = Usercredentials.password.data
    #     msg = ("username: {}\n Password: {}\n".format(us, pwd))
    return render_template("login0.html")


@app.route('/', methods=['GET', 'POST'])
def login():
    if flask_login.current_user.is_authenticated: # Check if the user is not already logged in
        return flask.redirect(url_for('index'))

    form = forms.LoginForm() # Load the form

    if form.validate_on_submit():
        # Retrieve the user with the username
        user = models.User.query.filter_by(username=form.username.data).first()

        # Check if it exist and if the password is the right password
        if user is None or not user.password == form.password.data:
            flask.flash('Invalid username or password')
            return flask.redirect(url_for('login'))

        # Log the user in
        flask_login.login_user(user, remember=form.remember_me.data)
        return flask.redirect(url_for('index'))

    return flask.render_template('login.html', title='Sign In', form=form) # Render the form