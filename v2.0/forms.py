from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class RegistrationForm(FlaskForm):
    Nom = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    Email = StringField('Email', validators=[DataRequired(), Email()])
    Prenom = StringField('First Name', validators=[DataRequired(), Length(max=100)])
    MDP = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('MDP')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    Nom = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    Email = StringField('Email', validators=[DataRequired(), Email()])
    Prenom = StringField('First Name', validators=[DataRequired(), Length(max=100)])
    MDP = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Login')
