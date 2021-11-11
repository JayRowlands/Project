from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SelectField, SubmitField

from application.models import Employee

class AddEmployee(FlaskForm):
    name = StringField("Name")
    role = SelectField("Role", choices = [('Breakfast Chef', 'Breakfast Chef'), ('Starter Chef', 'Starter Chef'), ('main_chef', 'Main Chef'), ('Dessert Chef', 'Dessert Chef')])
    email = StringField("Email")
    mobile_num = StringField("Mobile Number")
    submit = SubmitField("Add Employee")

class UpdateEmployee(FlaskForm):
    name = StringField("Name")
    role = SelectField("Role", choices = [('breakfast_chef', 'Breakfast Chef'), ('starter_chef', 'Starter Chef'), ('main_chef', 'Main Chef'), ('dessert_chef', 'Dessert Chef')])
    email = StringField("Email")
    mobile_num = StringField("Mobile Number")
    submit = SubmitField("Update Employee")

class AddOrder(FlaskForm):
    order_name = StringField("Order Name")
    cost = IntegerField("Cost")
    cust_name = StringField("Customer Name")
    employee_id = SelectField("Id", choice= [Employee.employee_id])
    submit = SubmitField("Add Order")

class UpdateOrder(FlaskForm):
    order_name = StringField("Order Name")
    cost = IntegerField("Cost")
    cust_name = StringField("Customer Name")
    employee_id = SelectField("Id", choice= [Employee.employee_id])
    submit = SubmitField("Update Order")