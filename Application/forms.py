from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField, TextAreaField, IntegerField, FloatField
from wtforms.validators import DataRequired, Length, ValidationError, Email, email_validator
from datetime import date

class CustomerForm(FlaskForm):
    Forename = StringField('Forename', validators=[DataRequired(), Length(min=1, max=30)])
    Surname = StringField('Surname', validators=[DataRequired(), Length(min=1, max=30)])
    Email = StringField('Email', validators=[DataRequired(), Email(), Length(min=5, max=30)])
    Address = StringField('Address', validators=[DataRequired(), Length(min=10, max=50)])
    Number = StringField ('Number')
    submit = SubmitField('Enter')

class BookForm(FlaskForm):
    ISBN = StringField('ISBN',validators=[DataRequired(), Length(min=13, max=13)])
    Title = StringField('Title', validators=[DataRequired(), Length(min=1, max=30)])
    Author = StringField('Author', validators=[DataRequired(), Length(min=1, max=30)])
    Genre = StringField('Genre')
    Rating = StringField('Rating')
    Price = FloatField('Price', validators=[DataRequired()])
    submit = SubmitField('Enter')

class DeleteBookName(FlaskForm):
     Title = StringField('Title', validators=[DataRequired(), Length(min=1, max=30)])
     submit = SubmitField('Enter')


class DeleteCustomerName(FlaskForm):
     Forename = StringField('Forename', validators=[DataRequired(), Length(min=1, max=30)])
     Surname = StringField('Surname', validators=[DataRequired(), Length(min=1, max=30)])
     submit = SubmitField('Enter')

class DeleteOrder(FlaskForm):
     OrderID = IntegerField('OrderID', validators=[DataRequired()])
     customerID = IntegerField('CustomerID',validators=[DataRequired()])
     submit = SubmitField('Enter')

class SearchCustomer(FlaskForm):
    Name = StringField("First Name", validators=[DataRequired()])
    submit = SubmitField('Enter')

class CreateOrder(FlaskForm):
     customerID = IntegerField('CustomerID',validators=[DataRequired()])
     orderDate = DateField ('Date placed', validators=[DataRequired()])
     submit = SubmitField('Enter')

class CreateBookOrder(FlaskForm):
     OrderID = IntegerField('Order ID' , validators=[DataRequired()])
     ISBN = StringField('ISBN', validators=[DataRequired(),Length(max = 13)])
     Quantity = IntegerField ('Quantity', validators=([DataRequired()]))
     submit = SubmitField('Enter')

class DeleteBookOrder(FlaskForm):
     BookOrderID = IntegerField('BookOrder ID', validators=[DataRequired()])
     submit = SubmitField('Enter')