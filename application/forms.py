from os import name
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from application.models import Employee
from application import db

class AddEmployee(FlaskForm):
    name = StringField("Name")
    role = SelectField("Role", choices = [('Breakfast Chef', 'Breakfast Chef'), ('Starter Chef', 'Starter Chef'), ('Main Chef', 'Main Chef'), ('Dessert Chef', 'Dessert Chef')])
    email = StringField("Email")
    mobile_num = StringField("Mobile Number")
    submit = SubmitField("Add Employee")

class UpdateEmployee(FlaskForm):
    name = StringField("Name")
    role = SelectField("Role", choices = [('Breakfast Chef', 'Breakfast Chef'), ('Starter Chef', 'Starter Chef'), ('Main Chef', 'Main Chef'), ('Dessert Chef', 'Dessert Chef')])
    email = StringField("Email")
    mobile_num = StringField("Mobile Number")
    submit = SubmitField("Update Employee")

class AddOrder(FlaskForm):
    order_name = StringField("Order Name")
    cost = StringField("Cost")
    cust_name = StringField("Customer Name")
    employee_id=QuerySelectField('Employee id' ,query_factory=lambda:Employee.query ,get_label="employee_id")
    submit = SubmitField("Add Order")

class UpdateOrder(FlaskForm):
    order_name = StringField("Order Name")
    cost = StringField("Cost")
    cust_name = StringField("Customer Name")
    employee_id=QuerySelectField('Employee id' ,query_factory=lambda:Employee.query, get_label="employee_id")
    submit = SubmitField("Add Order")