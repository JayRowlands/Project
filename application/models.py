from sqlalchemy.orm import relationship
from application import db

class Employees(db.model):
    employee_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(45))
    role = db.Column(db.String(45))
    email = db.Column(db.String(45))
    mobile_num = db.Column(db.Integer)
    orders = relationship(lambda: Orders)

class Orders(db.model):
    order_id = db.Column(db.Integer, primary_key = True)
    order_name = db.Column(db.String(45))
    cost = db.Column(db.Integer)
    cust_name = db.Column(db.String(45))
    employee_id = db.Column(db.Integer, db.ForeignKey(Employees.employee_id))