from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class RegistrationForm(FlaskForm):
    name=StringField("Full Name", validators=[DataRequired(message="Name is Required")])
    email=StringField("Email",validators=[DataRequired(message="Email is Required"),Email(message="Not a Valid Email")])
    password=PasswordField("Password",validators=[DataRequired("Password is Required"),Length(min=8, message="Password should be 8 Characters Long")])
    submit=SubmitField("Register")