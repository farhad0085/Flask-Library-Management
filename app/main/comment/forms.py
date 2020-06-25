# -*- coding:utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import Length, DataRequired


class CommentForm(FlaskForm):
    comment = TextAreaField("", validators=[DataRequired(), Length(1, 1024, message=u"Maximum 100 word!")])
    submit = SubmitField(u"Submit")
