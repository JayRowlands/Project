from application import app, db
from flask import render_template, request, redirect
from application.forms import AddEmployee, UpdateEmployee
from application.models import Employee

@app.route('/')
def home():
    employees = Employee.query.all()
    return render_template('homepage.html', records = employees)

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

@app.route("/filterRecords",methods=["POST"])
def filterRecords():
    if request.form["role"]=="all":
        return redirect("/")
    else:
        data = Employee.query.filter_by(role=request.form["role"]).all()
        return render_template("homepage.html",records=data)

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