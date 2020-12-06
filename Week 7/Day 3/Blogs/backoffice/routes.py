# First, we are in a different file, so we need to import the app
import flask
from backoffice import myapp    # app.app is package_name.variable_name


@myapp.route("/")
def index():

    return flask.render_template('indexbackoffice.html')