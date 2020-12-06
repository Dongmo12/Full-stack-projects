import flask_wtf
import wtforms

class Usercredentials(flask_wtf.FlaskForm):
    username = wtforms.StringField("Name")
    password = wtforms.PasswordField("Password")
    submit = wtforms.SubmitField("Submit")