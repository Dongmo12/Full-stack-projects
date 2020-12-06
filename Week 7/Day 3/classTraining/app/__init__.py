import flask

app = flask.Flask(__name__) # Remember: __name__ is the name of the file where the code is written
app.config['SECRET_KEY'] = 'you-will-never-guess'

from app import routes