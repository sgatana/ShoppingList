from flask_wtf import FlaskForm
from wtforms import  StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length, EqualTo
from wtforms.widgets import TextArea


class Login(FlaskForm):
    email = StringField('Username :', validators=[InputRequired(), Email(message='Invalid Email Address')])
    password = PasswordField('Password :', validators=[InputRequired(), Length(min=6, max=60)])
    remember = BooleanField('Remember me?')


class Register(FlaskForm):
    username = StringField('Username :', validators=[InputRequired(),Length(min=4, max=30)])
    email = StringField('Email :', validators=[InputRequired(), Email(message='Invalid Email Address')])
    password = PasswordField('Password :', validators=[InputRequired(), EqualTo('confirm', message='Password mismatch'),
                                                   Length(min=6, max=60)])
    confirm = PasswordField('Confirm Password :', validators=[InputRequired(), Length(min=6, max=60)])
    remember = BooleanField('By signing up, you agree with our terms and conditions')


class CreateShoppingList(FlaskForm):
    name = StringField("Name", validators=[InputRequired(), Length(min=4)])
    body = StringField("Description", widget=TextArea())


class AddItem(FlaskForm):
    ItemName = StringField(u'Item Name', validators=[InputRequired(), Length(min=3)])
    CatName = StringField('Category', validators = [InputRequired(), Length(min=3)] )
    price = StringField('Price', validators = [InputRequired(), Length(min = 3)])
    quantity = StringField('Quantity', validators = [InputRequired(), Length(min = 1)])