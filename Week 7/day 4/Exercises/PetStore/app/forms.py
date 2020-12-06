import flask_wtf import faskForm
import wtforms

class AddBookForm(flask_wtf.FlaskForm):
    title = wtforms.StringField("Title")
    author = wtforms.StringField("Author")
    price = wtforms.FloatField("Field")
    add = wtforms.SubmitField("Add New Book")