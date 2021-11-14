from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Employee, Order
from application.forms import AddEmployee, AddOrder, UpdateEmployee, UpdateOrder
import application.routes
from os import getenv

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:project_admin@34.105.227.92:3306/project',
            SECRET_KEY='secret_key',
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app

    def setUp(self):
        db.create_all()
        employeSample = Employee(name='John Smith', role='Breakfast Chef', email='email1@email.com', mobile_num='01234 567890')
        db.session.add(employeSample)
        orderSample = Order(order_name='order 1', cost=3.2, cust_name='Mike', employee_id='1')
        db.session.add(orderSample)
        db.session.commit()
        
    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestEmployees(TestBase):
    def test_get_employee(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'John Smith', response.data)
    
    def test_add_employee(self):
        response = self.client.post(
            url_for('saveEmployee'),
            data = dict(name='Tim Mile', role='Dessert Chef', email='34tim@mail.co.uk', mobile_num='43335 535677'),
            follow_redirects = True
        )
        self.assertIn(b'Tim Mile', response.data)
    
    def test_update_employee(self):
        response = self.client.post(
            url_for('editEmployee', employee_id=1),
            data = dict(name='Bob Smith', role='Breakfast Chef', email='email1@email.com', mobile_num='01234 567890'),
            follow_redirects = True
        )
        self.assertIn(b'Bob Smith', response.data)
    
    def test_delete_employee(self):
        response = self.client.get(url_for('deleteEmployee', employee_id=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Employee Information', response.data)
    
    def test_employee_info(self):
        response = self.client.get(url_for('employeeInformation', employee_id=1))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'John Smith', response.data)
    
    def test_view_edit(self):
        response = self.client.get(url_for('editEmployee', employee_id=1))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Name', response.data)
    
    def test_view_add(self):
        response = self.client.get(url_for('saveEmployee'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Name', response.data)
    
    def test_filter_records(self):
        response = self.client.post(url_for('filterRecords'),
        data = dict(role='Breakfast Chef'))
        self.assertIn(b'John Smith', response.data)
    
    def test_filter_all_records(self):
        response = self.client.post(url_for('filterRecords'),
        data = dict(role='all'),
        follow_redirects = True)
        self.assertIn(b'John Smith', response.data)

class TestOrders(TestBase):
    def test_get_order(self):
        response = self.client.get(url_for('viewOrders'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'order 1', response.data)
    
    def test_add_order(self):
        response = self.client.post(
            url_for('saveOrder'),
            data = dict(order_name='order 2', cost=2.3, cust_name='Nikk', employee_id='1'),
            follow_redirects = True
        )
        self.assertIn(b'order 2', response.data)
    
    def test_update_order(self):
        response = self.client.post(
            url_for('editOrder', order_id=1),
            data = dict(order_name='order 3', cost=3.2, cust_name='Mike', employee_id='1'),
            follow_redirects = True
        )
        self.assertIn(b'order 3', response.data)
    
    def test_delete_order(self):
        response = self.client.get(url_for('deleteOrder', order_id=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Order Information', response.data)
    
    def test_order_info(self):
        response = self.client.get(url_for('orderInformation', order_id=1))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'order 1', response.data)
    
    def test_view_edit(self):
        response = self.client.get(url_for('editOrder', order_id=1))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'order_name', response.data)
    
    def test_view_add(self):
        response = self.client.get(url_for('saveOrder'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'order_name', response.data)
    
    def test_filter_records(self):
        response = self.client.post(url_for('filterOrders'),
        data = dict(employee_id='1'))
        self.assertIn(b'order 1', response.data)
    
    def test_filter_all_records(self):
        response = self.client.post(url_for('filterOrders'),
        data = dict(employee_id='all'),
        follow_redirects = True)
        self.assertIn(b'order 1', response.data)