import flask
from flask import Flask, render_template

app = flask.Flask(__name__)


@app.route('/')
def index():
    return render_template('about.html')


# about-page
# @app.route('/about')
# def about():
#     return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000)
