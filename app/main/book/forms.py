# -*- coding:utf-8 -*-
from app.models import Book
from flask_pagedown.fields import PageDownField
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms import ValidationError
from wtforms.validators import Length, DataRequired, Regexp


class EditBookForm(FlaskForm):
    isbn = StringField(u"ISBN",
                       validators=[DataRequired(),
                                   Regexp('[0-9]{13,13}', message=u"ISBN must be 13 digits")])
    title = StringField(u"Title",
                        validators=[DataRequired(), Length(1, 128, message=u"Maximum 128 characters!")])
    origin_title = StringField(u"Origiinal Title", validators=[Length(0, 128, message=u"Maximum 128 characters!")])
    subtitle = StringField(u"Subtitle", validators=[Length(0, 128, message=u"Maximum 128 characters!")])
    author = StringField(u"Author", validators=[Length(0, 128, message=u"Maximum 128 characters!")])
    translator = StringField(u"Translator",
                             validators=[Length(0, 64, message=u"Maximum 64 characters!")])
    publisher = StringField(u"Publisher", validators=[Length(0, 64, message=u"Maximum 64 characters!")])
    image = StringField(u"Image", validators=[Length(0, 128, message=u"Maximum 128 characters!")])
    pubdate = StringField(u"Published Date", validators=[Length(0, 32, message=u"Maximum 32 characters!")])
    tags = StringField(u"Tags", validators=[Length(0, 128, message=u"Maximum 128 characters!")])
    pages = IntegerField(u"No. of page")
    price = StringField(u"Price", validators=[Length(0, 64, message=u"Maximum 64 characters!")])
    binding = StringField(u"Binding", validators=[Length(0, 16, message=u"Maximum 16 characters!")])
    numbers = IntegerField(u"Quantity", validators=[DataRequired()])
    summary = PageDownField(u"Summary")
    catalog = PageDownField(u"Catalog")
    submit = SubmitField(u"Save Changes")


class AddBookForm(EditBookForm):
    def validate_isbn(self, filed):
        if Book.query.filter_by(isbn=filed.data).count():
            raise ValidationError(u'The same ISBN already exists and cannot be entered, please check carefully whether the book is in stock.')


class SearchForm(FlaskForm):
    search = StringField(validators=[DataRequired()])
    submit = SubmitField(u"Search")


