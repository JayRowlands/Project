from application import app, db
from flask import render_template, request, redirect
from application.forms import AddEmployee, UpdateEmployee
from application.models import Employees

@app.route('/')
def home():
    employees = Employees.query_all()
    return render_template('homepage.html', records = employees)

@app.route('/edit_employee/<int:employee_id>', methods=['GET', 'POST'])
def edit_employee(employee_id):
    form = UpdateEmployee()
    employees = Employees.query.filter_by(employee_id=employee_id).first()
    if request.method == "POST":
        employees.name = form.name.data
        employees.role = form.role.data
        employees.email = form.role.data
        employees.mobile_num = form.mobile_num.data
        db.session.commit()
        return redirect('/')
    return render_template('edit_employee_form.html', form=form)

@app.route("/filter_records",methods=["POST"])
def filterrecords():
    if request.form["role"]=="all":
        return redirect("/")
    else:
        data = Employees.query.filter_by(dept=request.form["role"]).all()
        return render_template("homepage.html",records=data)

@app.route("/save_employee",methods=["GET","POST"])
def saveRecord():
    form = AddEmployee()
    if request.method == 'POST':
        name=form.emp_name.data
        role=form.role.data
        email=form.email.data
        mobile_num=form.mobile_num.data
        new_employee = Employees(name=name, role=role, email=email, mobile_num=mobile_num)
        db.session.add(new_employee)
        db.session.commit()
        return redirect("/")
    return render_template("input_employee_form.html", form=form)

@app.route("/employee_information/<int:employee_id>")
def personalInformation(employee_id):
	data = Employees.query.filter_by(employee_id=employee_id).first()
	return render_template("employee_information.html",record=data)

@app.route("/delete_employee/<int:empno>")
def deleteEmployee(employee_id):
    employee = Employees.query.filter_by(employee_id=employee_id).first()
    db.session.delete(employee)
    db.session.commit()
    return redirect("/")