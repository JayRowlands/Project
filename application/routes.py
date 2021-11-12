from application import app, db
from flask import render_template, request, redirect
from application.forms import AddEmployee, AddOrder, UpdateEmployee, UpdateOrder
from application.models import Employee, Order

@app.route('/')
def home():
    employees = Employee.query.all()
    return render_template('homepage.html', records = employees)

@app.route("/filterRecords",methods=["POST"])
def filterRecords():
    if request.form["role"]=="all":
        return redirect("/")
    else:
        data = Employee.query.filter_by(role=request.form["role"]).all()
        return render_template("homepage.html",records=data)

@app.route('/editEmployee/<int:employee_id>', methods=['GET', 'POST'])
def editEmployee(employee_id):
    form = UpdateEmployee()
    employees = Employee.query.filter_by(employee_id=employee_id).first()
    if request.method == "POST":
        employees.name = form.name.data
        employees.role = form.role.data
        employees.email = form.email.data
        employees.mobile_num = form.mobile_num.data
        db.session.commit()
        return redirect('/')
    return render_template('edit_employee_form.html', form=form)

@app.route("/saveEmployee",methods=["GET","POST"])
def saveEmployee():
    form = AddEmployee()
    if request.method == 'POST':
        name=form.name.data
        role=form.role.data
        email=form.email.data
        mobile_num=form.mobile_num.data
        new_employee = Employee(name=name, role=role, email=email, mobile_num=mobile_num)
        db.session.add(new_employee)
        db.session.commit()
        return redirect("/")
    return render_template("input_employee_form.html", form=form)

@app.route("/employeeInformation/<int:employee_id>")
def employeeInformation(employee_id):
	data = Employee.query.filter_by(employee_id=employee_id).first()
	return render_template("employee_information.html",record=data)

@app.route("/deleteEmployee/<int:employee_id>")
def deleteEmployee(employee_id):
    employee = Employee.query.filter_by(employee_id=employee_id).first()
    db.session.delete(employee)
    db.session.commit()
    return redirect("/")

@app.route("/viewOrders")
def viewOrders():
    orders = Order.query.all()
    return render_template('orders.html', records = orders)

@app.route("/filterOrders",methods=["POST"])
def filterOrders():
    if request.form["employee_id"]=="all":
        return redirect("/viewOrders")
    else:
        data = Order.query.filter_by(employee_id=request.form["employee_id"]).all()
        return render_template("orders.html",records=data)

@app.route('/editOrder/<int:order_id>', methods=['GET', 'POST'])
def editOrder(order_id):
    form = UpdateOrder()
    orders = Order.query.filter_by(order_id=order_id).first()
    if request.method == "POST":
        orders.order_name = form.order_name.data
        orders.cost = form.cost.data
        orders.cust_name = form.cust_name.data
        orders.employee_id = form.employee_id.data
        db.orders.commit()
        return redirect('/viewOrders')
    return render_template('edit_employee_form.html', form=form)

@app.route("/saveOrder",methods=["GET","POST"])
def saveOrder():
    form = AddOrder()
    if request.method == 'POST':
        order_name=form.order_name.data
        cost=form.cost.data
        cust_name=form.cust_name.data
        employee_string = filter(str.isdigit, str(form.employee_id.data))
        employee_id="".join(employee_string)
        new_order = Order(order_name=order_name, cost=cost, cust_name=cust_name, employee_id=employee_id)
        db.session.add(new_order)
        db.session.commit()
        return redirect("/viewOrders")
    return render_template("input_order_form.html", form=form)

@app.route("/orderInformation/<int:order_id>")
def orderInformation(order_id):
	data = Order.query.filter_by(order_id=order_id).first()
	return render_template("order_information.html",record=data)

@app.route("/deleteOrder/<int:order_id>")
def deleteOrder(order_id):
    orders = Order.query.filter_by(order_id=order_id).first()
    db.session.delete(orders)
    db.session.commit()
    return redirect("/viewOrders")