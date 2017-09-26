from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import  StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length

class Login(FlaskForm):
    email=StringField('username', validators=[InputRequired(), Email(message='Invalid Email Address')])
    password=PasswordField('password', validators=[InputRequired(), Length(min=6, max=60)])
    remember=BooleanField('Remember me?')

class Register(FlaskForm):
    username=StringField('username', validators=[InputRequired(),Length(min=4, max=30)])
    email=StringField('email', validators=[InputRequired(), Email(message='Invalid Email Address')])
    password=PasswordField('password', validators=[InputRequired(), Length(min=6, max=60)])
    confirm=PasswordField('confirm password', validators=[InputRequired(), Length(min=6, max=60)])
    remember=BooleanField('By signing up, you agree with our terms and conditions')
