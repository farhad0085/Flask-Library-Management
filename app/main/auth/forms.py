# -*- coding:utf-8 -*-
from app import db
from app.models import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms import ValidationError
from wtforms.validators import Email, Length, DataRequired, EqualTo


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(message=u"Please enter your email!"), Length(1, 64), Email(message=u"Incorrect email!")])
    password = PasswordField(u'Password', validators=[DataRequired(message=u"Please enter your password!")])
    remember_me = BooleanField(u"Keep me logged in", default=True)
    submit = SubmitField(u'Login')


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(message=u"Please enter your email!"), Length(1, 64), Email(message=u"Incorrect email!")])
    name = StringField(u'Username', validators=[DataRequired(message=u"Please enter your username!"), Length(4, 20, message="Please enter a username between 4-20 charecter!")])
    password = PasswordField(u'Password', validators=[DataRequired(message=u"Please enter your password!"), Length(6, 32, message="Please enter a password between 6-32 charecter!")])
    password2 = PasswordField(u'Confirm Password', validators=[DataRequired(message=u"Please enter your password!"), EqualTo('password', message=u'Passwords did not match!')])
    submit = SubmitField(u'Register')

    def validate_email(self, filed):
        if User.query.filter(db.func.lower(User.email) == db.func.lower(filed.data)).first():
            raise ValidationError(u'The email has already been registered!')


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField(u'Current Password', validators=[DataRequired(message=u"Enter your current password!")])
    new_password = PasswordField(u'New Password', validators=[DataRequired(message=u"Enter your new password!!"),
                                                     Length(6, 32)])
    confirm_password = PasswordField(u'Confirm Password', validators=[DataRequired(message=u"Enter your new password!!"), EqualTo('new_password', message=u'Password did not match!')])
    submit = SubmitField(u"Change Password")

    def validate_old_password(self, filed):
        from flask_login import current_user
        if not current_user.verify_password(filed.data):
            raise ValidationError(u'The current password is incorrect')
