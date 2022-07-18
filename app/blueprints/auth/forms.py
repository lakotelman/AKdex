from wtforms import Form,StringField,PasswordField,validators, SubmitField

from wtforms.validators import DataRequired, Email


class RegistrationForm(Form):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email Address", validators=[DataRequired()])
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Retype Password")
    submit_button = SubmitField("Create my account")
