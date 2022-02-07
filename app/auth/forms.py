# importing  the flask module that are used while creating a form

from enum import unique
from re import L
from flask_wtf import FlaskForm #the form from flask
from wtforms import StringField,BooleanField,PasswordField,SubmitField #the field class that we are going to use/import from the flask package wtform module module
from wtforms.validators import DataRequired,Email,EqualTo,Length,Regexp

class RegisterForm():
    '''
    class to create forms for registration and its input   
    '''
    username= StringField('Username',validators=[DataRequired(),Length(min=3,max=30,message='Provide a valid name'),Regexp('A-Za-z',message='Your name must contain letters only')])
    email=StringField(' Email',validators=[DataRequired(),Email(),Length(min=5,max=30)])
    password=PasswordField('Password',validators=[DataRequired(),EqualTo('confirmpassword',message='Password required to match'),Length(min=5,max=64)])
    confirmpassword=PasswordField('Confirm Password',validators=[DataRequired()])
    submit=SubmitField('Submit')
    
    
    
    
    
    
    
class LoginForm():
    '''
    class to create forms for login and its input   
    '''