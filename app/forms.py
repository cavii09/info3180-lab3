from email import message
from unicodedata import name
from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, validators, ValidationError
from wtforms.validators import DataRequired

class ContactForm(FlaskForm):
    name = StringField('Name', validators = [DataRequired()])
    email = StringField('Email', [ validators.DataRequired(), validators.Email("Please enter a valid email")])
    subject = StringField('Subject', validators = [DataRequired()])
    message = StringField('Message', validators =[DataRequired()])