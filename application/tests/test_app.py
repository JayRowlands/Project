from flask_testing import TestCase
from application import app, db
from application.models import Employee, Order
from application.forms import AddEmployee, AddOrder, UpdateEmployee, UpdateOrder
import application.routes
from os import getenv

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('db_uri'),
            SECRET_KEY=getenv('db_uri'),
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app

    def setUp(self):
        db.create_all()
        sample = Employee(name='John Smith', role='Breakfast Chef', email='email1@email.com', mobile_num='01234 567890')
        db.session.add(sample)
        db.session.commit()
        
    def tearDown(self):
        db.session.remove()
        db.drop_all()
