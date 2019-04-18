from flask import Flask, request, redirect, render_template
import sys
sys.path.insert(1, "PATH TO LOCAL PYTHON PACKAGES")  #OPTIONAL: Only if need to access Python packages installed on a local (non-global) directory
sys.path.insert(2, "PATH TO FLASK DIRECTORY")      #OPTIONAL: Only if you need to add the directory of your flask app

app = Flask(__name__)

@app.route('/')
@app.route('/home') 
def home():
    return render_template('home.html')   

@app.route('/doctors')
def doctors():
    from functions.sqlquery import sql_query
    results = sql_query('SELECT * FROM doctors')
    return render_template('doctors.html', results=results, page="Doctors")

@app.route('/doctors_insert',methods = ['POST', 'GET']) #this is when user submits an insert
def doctors_insert():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    query=""
    if request.method == 'POST':
        doctor_id = request.form['doctor_id']
        name = request.form['name']
        sex = request.form['sex']
        # age = request.form['age']
        phone = request.form['phone']
        dob = request.form['dob']
        dob=dob.split("-")
        dob=int(dob[2]+dob[1]+dob[0])
        degree = request.form['degree']
        address = request.form['address']
        dept_id = request.form['dept_id']
        desg_id = request.form['desg_id']
        query = 'INSERT INTO doctors VALUES ({},"{}",{},{},{},"{}","{}",{},{})'.format(doctor_id,name,sex,phone,dob,degree,address,dept_id,desg_id)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM doctors')
    return render_template('doctors.html', results=results, page="Doctors")

@app.route('/doctors_delete',methods = ['POST', 'GET']) #this is when user clicks delete link
def doctors_delete():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'GET':
        doctor_id = request.args.get('doctor_id')
        query='DELETE FROM doctors WHERE doctor_id={}'.format(doctor_id)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM doctors')
    return render_template('doctors.html', results=results, page="Doctors")
 
@app.route('/doctors_edit1',methods = ['POST', 'GET']) #this is when user clicks edit link
def doctors_edit1():
    from functions.sqlquery import sql_query
    if request.method == 'GET':
        doctor_id = request.args.get('doctor_id')
        eresults = sql_query('SELECT * FROM doctors WHERE doctor_id={}'.format(doctor_id))
    results = sql_query("SELECT * FROM doctors")
    return render_template('doctors.html', eresults=eresults, results=results, page="Doctors")

@app.route('/doctors_edit2',methods = ['POST', 'GET']) #this is when user submits an edit
def doctors_edit2():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'POST':
        old_doctor_id = request.form['old_doctor_id']
        doctor_id = request.form['doctor_id']
        name = request.form['name']
        sex = request.form['sex']
        # age = request.form['age']
        phone = request.form['phone']
        dob = request.form['dob']
        dob=dob.split("-")
        dob=int(dob[2]+dob[1]+dob[0])
        degree = request.form['degree']
        address = request.form['address']
        dept_id = request.form['dept_id']
        desg_id = request.form['desg_id']
        eresults = sql_query('SELECT * FROM doctors WHERE doctor_id={}'.format(doctor_id))
        query = 'UPDATE doctors set  doctor_id = {},name = "{}",sex = {},phone = {},dob = {},degree = "{}",address = "{}",dept_id = {},desg_id = {} WHERE doctor_id = {}'.format(doctor_id,name,sex,phone,dob,degree,address,dept_id,desg_id,old_doctor_id)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM doctors')
    return render_template('doctors.html', results=results, page="Doctors")

@app.route('/patients')
def patients():
    from functions.sqlquery import sql_query
    results = sql_query('SELECT * FROM patients')
    return render_template('patients.html', results=results, page="Patients")

@app.route('/patients_insert',methods = ['POST', 'GET']) #this is when user submits an insert
def patients_insert():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    query=""
    if request.method == 'POST':
        patient_id = request.form['patient_id']
        name = request.form['name']
        sex = request.form['sex']
        phone = request.form['phone']
        dob = request.form['dob']
        dob=dob.split("-")
        dob=int(dob[2]+dob[1]+dob[0])
        query = 'INSERT INTO patients VALUES ({},"{}",{},{},{})'.format(patient_id,name,sex,phone,dob)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM patients')
    return render_template('patients.html', results=results, page="Patients")

@app.route('/patients_delete',methods = ['POST', 'GET']) #this is when user clicks delete link
def patients_delete():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'GET':
        patient_id = request.args.get('patient_id')
        query='DELETE FROM patients WHERE patient_id={}'.format(patient_id)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM patients')
    return render_template('patients.html', results=results, page="Patients")

@app.route('/patients_edit1',methods = ['POST', 'GET']) #this is when user clicks edit link
def patients_edit1():
    from functions.sqlquery import sql_query
    if request.method == 'GET':
        patient_id = request.args.get('patient_id')
        eresults = sql_query('SELECT * FROM patients WHERE patient_id={}'.format(patient_id))
    results = sql_query("SELECT * FROM patients")
    return render_template('patients.html', eresults=eresults, results=results, page="Patients")

@app.route('/patients_edit2',methods = ['POST', 'GET']) #this is when user submits an edit
def patients_edit2():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'POST':
        old_patient_id = request.form['old_patient_id']
        patient_id = request.form['patient_id']
        name = request.form['name']
        sex = request.form['sex']
        phone = request.form['phone']
        dob = request.form['dob']
        dob=dob.split("-")
        dob=int(dob[2]+dob[1]+dob[0])
        eresults = sql_query('SELECT * FROM patients WHERE patient_id={}'.format(patient_id))
        query = 'UPDATE patients set  patient_id = {},name = "{}",sex = {},phone = {},dob = {} WHERE patient_id = {}'.format(patient_id,name,sex,phone,dob,old_patient_id)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM patients')
    return render_template('patients.html', results=results, page="Patients")

@app.route('/employee')
def employee():
    from functions.sqlquery import sql_query
    results = sql_query('SELECT * FROM employee')
    return render_template('employee.html', results=results, page="Employees")

@app.route('/employee_insert',methods = ['POST', 'GET']) #this is when user submits an insert
def employee_insert():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    query=""
    if request.method == 'POST':
        emp_id = request.form['emp_id']
        name = request.form['name']
        sex = request.form['sex']
        phone = request.form['phone']
        dob = request.form['dob']
        dob=dob.split("-")
        dob=int(dob[2]+dob[1]+dob[0])
        address = request.form['address']
        dept_id = request.form['dept_id']
        desg_id = request.form['desg_id']
        query = 'INSERT INTO employee VALUES ({},"{}",{},{},{},"{}",{},{})'.format(emp_id,name,sex,phone,dob,address,dept_id,desg_id)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM employee')
    return render_template('employee.html', results=results, page="Employees")

@app.route('/employee_delete',methods = ['POST', 'GET']) #this is when user clicks delete link
def employee_delete():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'GET':
        emp_id = request.args.get('emp_id')
        query='DELETE FROM employee WHERE emp_id={}'.format(emp_id)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM employee')
    return render_template('employee.html', results=results, page="Employees")

@app.route('/employee_edit1',methods = ['POST', 'GET']) #this is when user clicks edit link
def employee_edit1():
    from functions.sqlquery import sql_query
    if request.method == 'GET':
        emp_id = request.args.get('emp_id')
        eresults = sql_query('SELECT * FROM employee WHERE emp_id={}'.format(emp_id))
    results = sql_query("SELECT * FROM employee")
    return render_template('employee.html', eresults=eresults, results=results, page="Employees")

@app.route('/employee_edit2',methods = ['POST', 'GET']) #this is when user submits an edit
def employee_edit2():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'POST':
        old_emp_id = request.form['old_emp_id']
        emp_id = request.form['emp_id']
        name = request.form['name']
        sex = request.form['sex']
        phone = request.form['phone']
        dob = request.form['dob']
        dob=dob.split("-")
        dob=int(dob[2]+dob[1]+dob[0])
        address = request.form['address']
        dept_id = request.form['dept_id']
        desg_id = request.form['desg_id']
        eresults = sql_query('SELECT * FROM employee WHERE emp_id={}'.format(emp_id))
        query = 'UPDATE employee set  emp_id = {},name = "{}",sex = {},phone = {},dob = {},address = "{}",dept_id = {},desg_id = {} WHERE emp_id = {}'.format(emp_id,name,sex,phone,dob,address,dept_id,desg_id,old_emp_id)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM employee')
    return render_template('employee.html', results=results, page="Employees")

@app.route('/price_list')
def price_list():
    from functions.sqlquery import sql_query
    results = sql_query('SELECT * FROM price_list')
    return render_template('price_list.html', results=results, page="Price List")

@app.route('/price_list_insert',methods = ['POST', 'GET']) #this is when user submits an insert
def price_list_insert():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    query=""
    if request.method == 'POST':
        price_list_id = request.form['price_list_id']
        category = request.form['category']
        price = request.form['price']
        desc = request.form['desc']
        query = 'INSERT INTO price_list VALUES ({},{},{},{})'.format(price_list_id,category,price,desc)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM price_list')
    return render_template('price_list.html', results=results, page="Price List")

@app.route('/price_list_delete',methods = ['POST', 'GET']) #this is when user clicks delete link
def price_list_delete():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'GET':
        price_list_id = request.args.get('price_list_id')
        query='DELETE FROM price_list WHERE price_list_id={}'.format(price_list_id)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM price_list')
    return render_template('price_list.html', results=results, page="Price List")

@app.route('/price_list_edit1',methods = ['POST', 'GET']) #this is when user clicks edit link
def price_list_edit1():
    from functions.sqlquery import sql_query
    if request.method == 'GET':
        price_list_id = request.args.get('price_list_id')
        eresults = sql_query('SELECT * FROM price_list WHERE price_list_id={}'.format(price_list_id))
    results = sql_query("SELECT * FROM price_list")
    return render_template('price_list.html', eresults=eresults, results=results, page="Price List")

@app.route('/price_list_edit2',methods = ['POST', 'GET']) #this is when user submits an edit
def price_list_edit2():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'POST':
        old_price_list_id = request.form['old_price_list_id']
        price_list_id = request.form['price_list_id']
        category = request.form['category']
        price = request.form['price']
        desc = request.form['desc']
        eresults = sql_query('SELECT * FROM price_list WHERE price_list_id={}'.format(price_list_id))
        query = 'UPDATE price_list set  price_list_id = {},category = {},price = {},desc = "{}" WHERE price_list_id = {}'.format(price_list_id,category,price,desc,old_price_list_id)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM price_list')
    return render_template('price_list.html', results=results, page="Price List")


@app.route('/appointments')
def appointments():
    from functions.sqlquery import sql_query
    results = sql_query('SELECT * FROM appointments')
    return render_template('appointments.html', results=results, page="Appointments")

@app.route('/appointments_insert',methods = ['POST', 'GET']) #this is when user submits an insert
def appointments_insert():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    query=""
    if request.method == 'POST':
        doctor_id = request.form['doctor_id']
        patient_id = request.form['patient_id']
        date = request.form['date']
        date=date.split("-")
        date=int(date[2]+date[1]+date[0])
        time = request.form['time']
        temp = time.split(":")
        time=int(str(temp[0])+str(temp[1]))
        description = request.form['description']
        query = 'INSERT INTO appointments VALUES ({},{},{},{},"{}")'.format(doctor_id,patient_id,date,time,description)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM appointments')
    return render_template('appointments.html', results=results, page="Appointments")

@app.route('/appointments_delete',methods = ['POST', 'GET']) #this is when user clicks delete link
def appointments_delete():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'GET':
        doctor_id = request.args.get('doctor_id')
        patient_id = request.args.get('patient_id')
        date = request.args.get('date')
        # date=date.split("-")
        # date=int(date[2]+date[1]+date[0])
        time = request.args.get('time')
        # temp = time.split(":")
        # time=int(str(temp[0])+str(temp[1]))
        query='DELETE FROM appointments WHERE doctor_id={} AND patient_id={} AND date={} AND time={}'.format(doctor_id,patient_id,date,time)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM appointments')
    return render_template('appointments.html', results=results, page="Appointments")

@app.route('/appointments_edit1',methods = ['POST', 'GET']) #this is when user clicks edit link
def appointments_edit1():
    from functions.sqlquery import sql_query
    if request.method == 'GET':
        doctor_id = request.args.get('doctor_id')
        patient_id = request.args.get('patient_id')
        date = request.args.get('date')
        time = request.args.get('time')
        # print("AAAAAAAAAAAAAAAAAA")
        # temp = time.split(":")
        # time=int(str(temp[0])+str(temp[1]))
        eresults = sql_query('SELECT * FROM appointments WHERE doctor_id={} AND patient_id={} AND date={} AND time={}'.format(doctor_id,patient_id,date,time))
    results = sql_query("SELECT * FROM appointments")
    return render_template('appointments.html', eresults=eresults, results=results, page="Appointments")

@app.route('/appointments_edit2',methods = ['POST', 'GET']) #this is when user submits an edit
def appointments_edit2():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'POST':
        old_doctor_id = request.form['old_doctor_id']
        old_patient_id = request.form['old_patient_id']
        old_date = request.form['old_date']
        old_time = request.form['old_time']
        doctor_id = request.form['doctor_id']
        patient_id = request.form['patient_id']
        date = request.form['date']
        date=date.split("-")
        date=int(date[2]+date[1]+date[0])
        time = request.form['time']
        temp = time.split(":")
        time=int(str(temp[0])+str(temp[1]))
        description = request.form['description']
        eresults = sql_query('SELECT * FROM appointments WHERE doctor_id={} AND patient_id={} AND date={} AND time={}'.format(doctor_id,patient_id,date,time))
        query = 'UPDATE appointments set  doctor_id = {},patient_id = {},date = {},time = {},description = "{}" WHERE doctor_id = {} AND patient_id = {} AND date = {} AND time = {}'.format(doctor_id,patient_id,date,time,description,old_doctor_id,old_patient_id,old_date,old_time)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM appointments')
    return render_template('appointments.html', results=results, page="Appointments")

@app.route('/dept')
def dept():
    from functions.sqlquery import sql_query
    results = sql_query('SELECT * FROM dept')
    return render_template('dept.html', results=results, page="Departments")

@app.route('/dept_insert',methods = ['POST', 'GET']) #this is when user submits an insert
def dept_insert():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    query=""
    if request.method == 'POST':
        dept_id = request.form['dept_id']
        name = request.form['name']
        doctor_id = request.form['doctor_id']
        query = 'INSERT INTO dept VALUES ({},"{}",{})'.format(dept_id,name,doctor_id)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM dept')
    return render_template('dept.html', results=results, page="Departments")

@app.route('/dept_delete',methods = ['POST', 'GET']) #this is when user clicks delete link
def dept_delete():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'GET':
        dept_id = request.args.get('dept_id')
        query='DELETE FROM dept WHERE dept_id={}'.format(dept_id)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM dept')
    return render_template('dept.html', results=results, page="Departments")

@app.route('/dept_edit1',methods = ['POST', 'GET']) #this is when user clicks edit link
def dept_edit1():
    from functions.sqlquery import sql_query
    if request.method == 'GET':
        dept_id = request.args.get('dept_id')
        eresults = sql_query('SELECT * FROM dept WHERE dept_id={}'.format(dept_id))
    results = sql_query("SELECT * FROM dept")
    return render_template('dept.html', eresults=eresults, results=results, page="Departments")

@app.route('/dept_edit2',methods = ['POST', 'GET']) #this is when user submits an edit
def dept_edit2():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'POST':
        old_dept_id = request.form['old_dept_id']
        dept_id = request.form['dept_id']
        name = request.form['name']
        doctor_id = request.form['doctor_id']
        eresults = sql_query('SELECT * FROM dept WHERE dept_id={}'.format(dept_id))
        query = 'UPDATE dept set  dept_id = {},name = "{}",doctor_id = {} WHERE dept_id = {}'.format(dept_id,name,doctor_id,old_dept_id)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM dept')
    return render_template('dept.html', results=results, page="Departments")

@app.route('/desg')
def desg():
    from functions.sqlquery import sql_query
    results = sql_query('SELECT * FROM desg')
    return render_template('desg.html', results=results, page="Designations")

@app.route('/desg_insert',methods = ['POST', 'GET']) #this is when user submits an insert
def desg_insert():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    query=""
    if request.method == 'POST':
        desg_id = request.form['desg_id']
        name = request.form['name']
        salary = request.form['salary']
        dept_id = request.form['dept_id']
        query = 'INSERT INTO desg VALUES ({},"{}",{},{})'.format(desg_id,name,salary,dept_id)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM desg')
    return render_template('desg.html', results=results, page="Designations")

@app.route('/desg_delete',methods = ['POST', 'GET']) #this is when user clicks delete link
def desg_delete():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'GET':
        desg_id = request.args.get('desg_id')
        query='DELETE FROM desg WHERE desg_id={}'.format(desg_id)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM desg')
    return render_template('desg.html', results=results, page="Designations")

@app.route('/desg_edit1',methods = ['POST', 'GET']) #this is when user clicks edit link
def desg_edit1():
    from functions.sqlquery import sql_query
    if request.method == 'GET':
        desg_id = request.args.get('desg_id')
        eresults = sql_query('SELECT * FROM desg WHERE desg_id={}'.format(desg_id))
    results = sql_query("SELECT * FROM desg")
    return render_template('desg.html', eresults=eresults, results=results, page="Designations")

@app.route('/desg_edit2',methods = ['POST', 'GET']) #this is when user submits an edit
def desg_edit2():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'POST':
        old_desg_id = request.form['old_desg_id']
        desg_id = request.form['desg_id']
        name = request.form['name']
        salary = request.form['salary']
        dept_id = request.form['dept_id']
        eresults = sql_query('SELECT * FROM desg WHERE desg_id={}'.format(desg_id))
        query = 'UPDATE desg set  desg_id = {},name = "{}",salary = {},dept_id = {} WHERE desg_id = {}'.format(desg_id,name,salary,dept_id,old_desg_id)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM desg')
    return render_template('desg.html', results=results, page="Designations")


@app.route('/inventory')
def inventory():
    from functions.sqlquery import sql_query
    results = sql_query('SELECT * FROM inventory')
    return render_template('inventory.html', results=results, page="Inventory")

@app.route('/inventory_insert',methods = ['POST', 'GET']) #this is when user submits an insert
def inventory_insert():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    query=""
    if request.method == 'POST':
        equip_id = request.form['equip_id']
        dept_id = request.form['dept_id']
        name = request.form['name']
        quantity = request.form['quantity']
        query = 'INSERT INTO inventory VALUES ({},{},{},{})'.format(equip_id,dept_id,name,quantity)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM inventory')
    return render_template('inventory.html', results=results, page="Inventory")

@app.route('/inventory_delete',methods = ['POST', 'GET']) #this is when user clicks delete link
def inventory_delete():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'GET':
        equip_id = request.args.get('equip_id')
        dept_id = request.args.get('dept_id')
        query='DELETE FROM inventory WHERE equip_id={} AND dept_id={}'.format(equip_id,dept_id)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM inventory')
    return render_template('inventory.html', results=results, page="Inventory")

@app.route('/inventory_edit1',methods = ['POST', 'GET']) #this is when user clicks edit link
def inventory_edit1():
    from functions.sqlquery import sql_query
    if request.method == 'GET':
        equip_id = request.args.get('equip_id')
        dept_id = request.args.get('dept_id')
        eresults = sql_query('SELECT * FROM inventory WHERE equip_id={} AND dept_id={}'.format(equip_id,dept_id))
    results = sql_query("SELECT * FROM inventory")
    return render_template('inventory.html', eresults=eresults, results=results, page="Inventory")

@app.route('/inventory_edit2',methods = ['POST', 'GET']) #this is when user submits an edit
def inventory_edit2():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'POST':
        old_equip_id = request.form['old_equip_id']
        old_dept_id = request.form['old_dept_id']
        equip_id = request.form['equip_id']
        dept_id = request.form['dept_id']
        name = request.form['name']
        quantity = request.form['quantity']
        eresults = sql_query('SELECT * FROM inventory WHERE equip_id={} AND dept_id={}'.format(equip_id,dept_id))
        query = 'UPDATE inventory set  equip_id = {},dept_id = {},name = {},quantity = {} WHERE equip_id = {} AND dept_id = {}'.format(equip_id,dept_id,name,quantity,old_equip_id,old_dept_id)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM inventory')
    return render_template('inventory.html', results=results, page="Inventory")

@app.route('/visiting')
def visiting():
    from functions.sqlquery import sql_query
    results = sql_query('SELECT * FROM visiting')
    return render_template('visiting.html', results=results, page="Visits")

@app.route('/visiting_insert',methods = ['POST', 'GET']) #this is when user submits an insert
def visiting_insert():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    query=""
    if request.method == 'POST':
        time_in = request.form['time_in']
        temp = time_in.split(":")
        time_in=int(str(temp[0])+str(temp[1]))
        time_out = request.form['time_out']
        time_out = request.form['time_out']
        temp = time_out.split(":")
        time_out=int(str(temp[0])+str(temp[1]))
        patient_id = request.form['patient_id']
        visitor_id = request.form['visitor_id']
        query = 'INSERT INTO visiting VALUES ({},{},{},{})'.format(time_in,time_out,patient_id,visitor_id)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM visiting')
    return render_template('visiting.html', results=results, page="Visits")

@app.route('/visiting_delete',methods = ['POST', 'GET']) #this is when user clicks delete link
def visiting_delete():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'GET':
        time_in = request.args.get('time_in')
        # temp = time_in.split(":")
        # time_in=int(str(temp[0])+str(temp[1]))
        time_out = request.args.get('time_out')
        # temp = time_out.split(":")
        # time_out=int(str(temp[0])+str(temp[1]))
        patient_id = request.args.get('patient_id')
        visitor_id = request.args.get('visitor_id')
        query='DELETE FROM visiting WHERE time_in={} AND time_out={} AND patient_id={} AND visitor_id={}'.format(time_in,time_out,patient_id,visitor_id)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM visiting')
    return render_template('visiting.html', results=results, page="Visits")

@app.route('/visiting_edit1',methods = ['POST', 'GET']) #this is when user clicks edit link
def visiting_edit1():
    from functions.sqlquery import sql_query
    if request.method == 'GET':
        time_in = request.args.get('time_in')
        # temp = time_in.split(":")
        # time_in=int(str(temp[0])+str(temp[1]))
        time_out = request.args.get('time_out')
        # temp = time_out.split(":")
        # time_out=int(str(temp[0])+str(temp[1]))
        patient_id = request.args.get('patient_id')
        visitor_id = request.args.get('visitor_id')
        eresults = sql_query('SELECT * FROM visiting WHERE time_in={} AND time_out={} AND patient_id={} AND visitor_id={}'.format(time_in,time_out,patient_id,visitor_id))
    results = sql_query("SELECT * FROM visiting")
    return render_template('visiting.html', eresults=eresults, results=results, page="Visits")

@app.route('/visiting_edit2',methods = ['POST', 'GET']) #this is when user submits an edit
def visiting_edit2():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'POST':
        old_time_in = request.form['old_time_in']
        # temp = old_time_in.split(":")
        # old_time_in=int(str(temp[0])+str(temp[1]))
        old_time_out = request.form['old_time_out']
        # temp = old_time_out.split(":")
        # old_time_out=int(str(temp[0])+str(temp[1]))
        old_patient_id = request.form['old_patient_id']
        old_visitor_id = request.form['old_visitor_id']
        time_in = request.form['time_in']
        temp = time_in.split(":")
        time_in=int(str(temp[0])+str(temp[1]))
        time_out = request.form['time_out']
        temp = time_out.split(":")
        time_out=int(str(temp[0])+str(temp[1]))
        patient_id = request.form['patient_id']
        visitor_id = request.form['visitor_id']
        eresults = sql_query('SELECT * FROM visiting WHERE time_in={} AND time_out={} AND patient_id={} AND visitor_id={}'.format(time_in,time_out,patient_id,visitor_id))
        query = 'UPDATE visiting set  time_in = {},time_out = {},patient_id = {},visitor_id = {} WHERE time_in = {} AND time_out = {} AND patient_id = {} AND visitor_id = {}'.format(time_in,time_out,patient_id,visitor_id,old_time_in,old_time_out,old_patient_id,old_visitor_id)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM visiting')
    return render_template('visiting.html', results=results, page="Visits")

@app.route('/lib_issued')
def lib_issued():
    from functions.sqlquery import sql_query
    results = sql_query('SELECT * FROM lib_issued')
    return render_template('lib_issued.html', results=results, page="Books Issued")

@app.route('/lib_issued_insert',methods = ['POST', 'GET']) #this is when user submits an insert
def lib_issued_insert():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    query=""
    if request.method == 'POST':
        issue_date = request.form['issue_date']
        issue_date=issue_date.split("-")
        issue_date=int(issue_date[2]+issue_date[1]+issue_date[0])
        book_id = request.form['book_id']
        return_status = request.form['return_status']
        return_date = request.form['return_date']
        return_date=return_date.split("-")
        return_date=int(return_date[2]+return_date[1]+return_date[0])
        doctor_id = request.form['doctor_id']
        roll_no = request.form['roll_no']
        emp_id = request.form['emp_id']
        query = 'INSERT INTO lib_issued VALUES ({},{},{},{},{},{},{})'.format(issue_date,book_id,return_status,return_date,doctor_id,roll_no,emp_id)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM lib_issued')
    return render_template('lib_issued.html', results=results, page="Books Issued")

@app.route('/lib_issued_delete',methods = ['POST', 'GET']) #this is when user clicks delete link
def lib_issued_delete():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'GET':
        issue_date = request.args.get('issue_date')
        book_id = request.args.get('book_id')
        query='DELETE FROM lib_issued WHERE issue_date={} AND book_id={}'.format(issue_date,book_id)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM lib_issued')
    return render_template('lib_issued.html', results=results, page="Books Issued")

@app.route('/lib_issued_edit1',methods = ['POST', 'GET']) #this is when user clicks edit link
def lib_issued_edit1():
    from functions.sqlquery import sql_query
    if request.method == 'GET':
        issue_date = request.args.get('issue_date')
        book_id = request.args.get('book_id')
        eresults = sql_query('SELECT * FROM lib_issued WHERE issue_date={} AND book_id={}'.format(issue_date,book_id))
    results = sql_query("SELECT * FROM lib_issued")
    return render_template('lib_issued.html', eresults=eresults, results=results, page="Books Issued")

@app.route('/lib_issued_edit2',methods = ['POST', 'GET']) #this is when user submits an edit
def lib_issued_edit2():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'POST':
        old_issue_date = request.form['old_issue_date']
        old_issue_date=old_issue_date.split("-")
        old_issue_date=int(old_issue_date[2]+old_issue_date[1]+old_issue_date[0])
        old_book_id = request.form['old_book_id']
        issue_date = request.form['issue_date']
        issue_date=issue_date.split("-")
        issue_date=int(issue_date[2]+issue_date[1]+issue_date[0])
        book_id = request.form['book_id']
        return_status = request.form['return_status']
        return_date = request.form['return_date']
        return_date=return_date.split("-")
        return_date=int(return_date[2]+return_date[1]+return_date[0])
        doctor_id = request.form['doctor_id']
        roll_no = request.form['roll_no']
        emp_id = request.form['emp_id']
        eresults = sql_query('SELECT * FROM lib_issued WHERE issue_date={} AND book_id={}'.format(issue_date,book_id))
        query = 'UPDATE lib_issued set  issue_date = {},book_id = {},return_status = {},return_date = {},doctor_id = {},roll_no = {},emp_id = {} WHERE issue_date = {} AND book_id = {}'.format(issue_date,book_id,return_status,return_date,doctor_id,roll_no,emp_id,old_issue_date,old_book_id)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM lib_issued')
    return render_template('lib_issued.html', results=results, page="Books Issued")

@app.route('/vendors')
def vendors():
    from functions.sqlquery import sql_query
    results = sql_query('SELECT * FROM vendors')
    return render_template('vendors.html', results=results, page="Vendors")

@app.route('/vendors_insert',methods = ['POST', 'GET']) #this is when user submits an insert
def vendors_insert():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    query=""
    if request.method == 'POST':
        vendor_id = request.form['vendor_id']
        name = request.form['name']
        phone = request.form['phone']
        query = 'INSERT INTO vendors VALUES ({},"{}",{})'.format(vendor_id,name,phone)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM vendors')
    return render_template('vendors.html', results=results, page="Vendors")

@app.route('/vendors_delete',methods = ['POST', 'GET']) #this is when user clicks delete link
def vendors_delete():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'GET':
        vendor_id = request.args.get('vendor_id')
        query='DELETE FROM vendors WHERE vendor_id={}'.format(vendor_id)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM vendors')
    return render_template('vendors.html', results=results, page="Vendors")

@app.route('/vendors_edit1',methods = ['POST', 'GET']) #this is when user clicks edit link
def vendors_edit1():
    from functions.sqlquery import sql_query
    if request.method == 'GET':
        vendor_id = request.args.get('vendor_id')
        eresults = sql_query('SELECT * FROM vendors WHERE vendor_id={}'.format(vendor_id))
    results = sql_query("SELECT * FROM vendors")
    return render_template('vendors.html', eresults=eresults, results=results, page="Vendors")

@app.route('/vendors_edit2',methods = ['POST', 'GET']) #this is when user submits an edit
def vendors_edit2():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'POST':
        old_vendor_id = request.form['old_vendor_id']
        vendor_id = request.form['vendor_id']
        name = request.form['name']
        phone = request.form['phone']
        eresults = sql_query('SELECT * FROM vendors WHERE vendor_id={}'.format(vendor_id))
        query = 'UPDATE vendors set  vendor_id = {},name = "{}",phone = {} WHERE vendor_id = {}'.format(vendor_id,name,phone,old_vendor_id)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM vendors')
    return render_template('vendors.html', results=results, page="Vendors")

@app.route('/insurance')
def insurance():
    from functions.sqlquery import sql_query
    results = sql_query('SELECT * FROM insurance')
    return render_template('insurance.html', results=results, page="Insurance")

@app.route('/insurance_insert',methods = ['POST', 'GET']) #this is when user submits an insert
def insurance_insert():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    query=""
    if request.method == 'POST':
        insurance_id = request.form['insurance_id']
        name = request.form['name']
        company_name = request.form['company_name']
        amount = request.form['amount']
        receiver_id = request.form['receiver_id']
        receiver_name = request.form['receiver_name']
        query = 'INSERT INTO insurance VALUES ({},"{}","{}",{},{},"{}")'.format(insurance_id,name,company_name,amount,receiver_id,receiver_name)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM insurance')
    return render_template('insurance.html', results=results, page="Insurance")

@app.route('/insurance_delete',methods = ['POST', 'GET']) #this is when user clicks delete link
def insurance_delete():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'GET':
        insurance_id = request.args.get('insurance_id')
        query='DELETE FROM insurance WHERE insurance_id={}'.format(insurance_id)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM insurance')
    return render_template('insurance.html', results=results, page="Insurance")

@app.route('/insurance_edit1',methods = ['POST', 'GET']) #this is when user clicks edit link
def insurance_edit1():
    from functions.sqlquery import sql_query
    if request.method == 'GET':
        insurance_id = request.args.get('insurance_id')
        eresults = sql_query('SELECT * FROM insurance WHERE insurance_id={}'.format(insurance_id))
    results = sql_query("SELECT * FROM insurance")
    return render_template('insurance.html', eresults=eresults, results=results, page="Insurance")

@app.route('/insurance_edit2',methods = ['POST', 'GET']) #this is when user submits an edit
def insurance_edit2():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'POST':
        old_insurance_id = request.form['old_insurance_id']
        insurance_id = request.form['insurance_id']
        name = request.form['name']
        company_name = request.form['company_name']
        amount = request.form['amount']
        receiver_id = request.form['receiver_id']
        receiver_name = request.form['receiver_name']
        eresults = sql_query('SELECT * FROM insurance WHERE insurance_id={}'.format(insurance_id))
        query = 'UPDATE insurance set  insurance_id = {},name = "{}",company_name = "{}",amount = {},receiver_id = {},receiver_name = "{}" WHERE insurance_id = {}'.format(insurance_id,name,company_name,amount,receiver_id,receiver_name,old_insurance_id)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM insurance')
    return render_template('insurance.html', results=results, page="Insurance")

@app.route('/library')
def library():
    from functions.sqlquery import sql_query
    results = sql_query('SELECT * FROM library')
    return render_template('library.html', results=results, page="Library")

@app.route('/library_insert',methods = ['POST', 'GET']) #this is when user submits an insert
def library_insert():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    query=""
    if request.method == 'POST':
        book_id = request.form['book_id']
        book_name = request.form['book_name']
        edition = request.form['edition']
        quantity = request.form['quantity']
        query = 'INSERT INTO library VALUES ({},"{}",{},{})'.format(book_id,book_name,edition,quantity)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM library')
    return render_template('library.html', results=results, page="Library")

@app.route('/library_delete',methods = ['POST', 'GET']) #this is when user clicks delete link
def library_delete():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'GET':
        book_id = request.args.get('book_id')
        query='DELETE FROM library WHERE book_id={}'.format(book_id)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM library')
    return render_template('library.html', results=results, page="Library")

@app.route('/library_edit1',methods = ['POST', 'GET']) #this is when user clicks edit link
def library_edit1():
    from functions.sqlquery import sql_query
    if request.method == 'GET':
        book_id = request.args.get('book_id')
        eresults = sql_query('SELECT * FROM library WHERE book_id={}'.format(book_id))
    results = sql_query("SELECT * FROM library")
    return render_template('library.html', eresults=eresults, results=results, page="Library")

@app.route('/library_edit2',methods = ['POST', 'GET']) #this is when user submits an edit
def library_edit2():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'POST':
        old_book_id = request.form['old_book_id']
        book_id = request.form['book_id']
        book_name = request.form['book_name']
        edition = request.form['edition']
        quantity = request.form['quantity']
        eresults = sql_query('SELECT * FROM library WHERE book_id={}'.format(book_id))
        query = 'UPDATE library set  book_id = {},book_name = "{}",edition = {},quantity = {} WHERE book_id = {}'.format(book_id,book_name,edition,quantity,old_book_id)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM library')
    return render_template('library.html', results=results, page="Library")


@app.route('/visitor')
def visitor():
    from functions.sqlquery import sql_query
    results = sql_query('SELECT * FROM visitor')
    return render_template('visitor.html', results=results, page="Visitors")

@app.route('/visitor_insert',methods = ['POST', 'GET']) #this is when user submits an insert
def visitor_insert():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    query=""
    if request.method == 'POST':
        visitor_id = request.form['visitor_id']
        name = request.form['name']
        phone = request.form['phone']
        sex = request.form['sex']
        age = request.form['age']
        query = 'INSERT INTO visitor VALUES ({},"{}",{},{},{})'.format(visitor_id,name,phone,sex,age)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM visitor')
    return render_template('visitor.html', results=results, page="Visitors")

@app.route('/visitor_delete',methods = ['POST', 'GET']) #this is when user clicks delete link
def visitor_delete():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'GET':
        visitor_id = request.args.get('visitor_id')
        query='DELETE FROM visitor WHERE visitor_id={}'.format(visitor_id)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM visitor')
    return render_template('visitor.html', results=results, page="Visitors")

@app.route('/visitor_edit1',methods = ['POST', 'GET']) #this is when user clicks edit link
def visitor_edit1():
    from functions.sqlquery import sql_query
    if request.method == 'GET':
        visitor_id = request.args.get('visitor_id')
        eresults = sql_query('SELECT * FROM visitor WHERE visitor_id={}'.format(visitor_id))
    results = sql_query("SELECT * FROM visitor")
    return render_template('visitor.html', eresults=eresults, results=results, page="Visitors")

@app.route('/visitor_edit2',methods = ['POST', 'GET']) #this is when user submits an edit
def visitor_edit2():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'POST':
        old_visitor_id = request.form['old_visitor_id']
        visitor_id = request.form['visitor_id']
        name = request.form['name']
        phone = request.form['phone']
        sex = request.form['sex']
        age = request.form['age']
        eresults = sql_query('SELECT * FROM visitor WHERE visitor_id={}'.format(visitor_id))
        query = 'UPDATE visitor set  visitor_id = {},name = "{}",phone = {},sex = {},age = {} WHERE visitor_id = {}'.format(visitor_id,name,phone,sex,age,old_visitor_id)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM visitor')
    return render_template('visitor.html', results=results, page="Visitors")

@app.route('/students')
def students():
    from functions.sqlquery import sql_query
    results = sql_query('SELECT * FROM students')
    return render_template('students.html', results=results, page="Student Search")

@app.route('/students_insert',methods = ['POST', 'GET']) #this is when user submits an insert
def students_insert():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    query=""
    if request.method == 'POST':
        roll_no = request.form['roll_no']
        name = request.form['name']
        degree = request.form['degree']
        year = request.form['year']
        sex = request.form['sex']
        phone = request.form['phone']
        dob = request.form['dob']
        dob=dob.split("-")
        dob=int(dob[2]+dob[1]+dob[0])
        address = request.form['address']
        query = 'INSERT INTO students VALUES ({},"{}","{}",{},{},{},{},"{}")'.format(roll_no,name,degree,year,sex,phone,dob,address)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM students')
    return render_template('students.html', results=results, page="Student Search")

@app.route('/students_delete',methods = ['POST', 'GET']) #this is when user clicks delete link
def students_delete():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'GET':
        roll_no = request.args.get('roll_no')
        query='DELETE FROM students WHERE roll_no={}'.format(roll_no)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM students')
    return render_template('students.html', results=results, page="Student Search")

@app.route('/students_edit1',methods = ['POST', 'GET']) #this is when user clicks edit link
def students_edit1():
    from functions.sqlquery import sql_query
    if request.method == 'GET':
        roll_no = request.args.get('roll_no')
        eresults = sql_query('SELECT * FROM students WHERE roll_no={}'.format(roll_no))
    results = sql_query("SELECT * FROM students")
    return render_template('students.html', eresults=eresults, results=results, page="Student Search")

@app.route('/students_edit2',methods = ['POST', 'GET']) #this is when user submits an edit
def students_edit2():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'POST':
        old_roll_no = request.form['old_roll_no']
        roll_no = request.form['roll_no']
        name = request.form['name']
        degree = request.form['degree']
        year = request.form['year']
        sex = request.form['sex']
        phone = request.form['phone']
        dob = request.form['dob']
        dob=dob.split("-")
        dob=int(dob[2]+dob[1]+dob[0])
        address = request.form['address']
        eresults = sql_query('SELECT * FROM students WHERE roll_no={}'.format(roll_no))
        query = 'UPDATE students set  roll_no = {},name = "{}",degree = "{}",year = {},sex = {},phone = {},dob = {},address = "{}" WHERE roll_no = {}'.format(roll_no,name,degree,year,sex,phone,dob,address,old_roll_no)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM students')
    return render_template('students.html', results=results, page="Student Search")

@app.route('/ambulances')
def ambulances():
    from functions.sqlquery import sql_query
    results = sql_query('SELECT * FROM ambulances')
    return render_template('ambulances.html', results=results, page="Ambulances")

@app.route('/ambulances_insert',methods = ['POST', 'GET']) #this is when user submits an insert
def ambulances_insert():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    query=""
    if request.method == 'POST':
        vehicle_no = request.form['vehicle_no']
        emp_id = request.form['emp_id']
        model_name = request.form['model_name']
        type = request.form['type']
        query = 'INSERT INTO ambulances VALUES ({},{},"{}","{}")'.format(vehicle_no,emp_id,model_name,type)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM ambulances')
    return render_template('ambulances.html', results=results, page="Ambulances")

@app.route('/ambulances_delete',methods = ['POST', 'GET']) #this is when user clicks delete link
def ambulances_delete():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'GET':
        vehicle_no = request.args.get('vehicle_no')
        emp_id = request.args.get('emp_id')
        query='DELETE FROM ambulances WHERE vehicle_no={} AND emp_id={}'.format(vehicle_no,emp_id)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM ambulances')
    return render_template('ambulances.html', results=results, page="Ambulances")

@app.route('/ambulances_edit1',methods = ['POST', 'GET']) #this is when user clicks edit link
def ambulances_edit1():
    from functions.sqlquery import sql_query
    if request.method == 'GET':
        vehicle_no = request.args.get('vehicle_no')
        emp_id = request.args.get('emp_id')
        eresults = sql_query('SELECT * FROM ambulances WHERE vehicle_no={} AND emp_id={}'.format(vehicle_no,emp_id))
    results = sql_query("SELECT * FROM ambulances")
    return render_template('ambulances.html', eresults=eresults, results=results, page="Ambulances")

@app.route('/ambulances_edit2',methods = ['POST', 'GET']) #this is when user submits an edit
def ambulances_edit2():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'POST':
        old_vehicle_no = request.form['old_vehicle_no']
        old_emp_id = request.form['old_emp_id']
        vehicle_no = request.form['vehicle_no']
        emp_id = request.form['emp_id']
        model_name = request.form['model_name']
        type = request.form['type']
        eresults = sql_query('SELECT * FROM ambulances WHERE vehicle_no={} AND emp_id={}'.format(vehicle_no,emp_id))
        query = 'UPDATE ambulances set  vehicle_no = {},emp_id = {},model_name = "{}",type = "{}" WHERE vehicle_no = {} AND emp_id = {}'.format(vehicle_no,emp_id,model_name,type,old_vehicle_no,old_emp_id)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM ambulances')
    return render_template('ambulances.html', results=results, page="Ambulances")

@app.route('/student_doc')
def student_doc():
    from functions.sqlquery import sql_query
    results = sql_query('SELECT * FROM student_doc')
    return render_template('student_doc.html', results=results, page="Students-Doctor Supervisors")

@app.route('/student_doc_insert',methods = ['POST', 'GET']) #this is when user submits an insert
def student_doc_insert():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    query=""
    if request.method == 'POST':
        roll_no = request.form['roll_no']
        doctor_id = request.form['doctor_id']
        term = request.form['term']
        field = request.form['field']
        dept_id = request.form['dept_id']
        query = 'INSERT INTO student_doc VALUES ({},{},{},"{}",{})'.format(roll_no,doctor_id,term,field,dept_id)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM student_doc')
    return render_template('student_doc.html', results=results, page="Students-Doctor Supervisors")

@app.route('/student_doc_delete',methods = ['POST', 'GET']) #this is when user clicks delete link
def student_doc_delete():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'GET':
        roll_no = request.args.get('roll_no')
        doctor_id = request.args.get('doctor_id')
        query='DELETE FROM student_doc WHERE roll_no={} AND doctor_id={}'.format(roll_no,doctor_id)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM student_doc')
    return render_template('student_doc.html', results=results, page="Students-Doctor Supervisors")

@app.route('/student_doc_edit1',methods = ['POST', 'GET']) #this is when user clicks edit link
def student_doc_edit1():
    from functions.sqlquery import sql_query
    if request.method == 'GET':
        roll_no = request.args.get('roll_no')
        doctor_id = request.args.get('doctor_id')
        eresults = sql_query('SELECT * FROM student_doc WHERE roll_no={} AND doctor_id={}'.format(roll_no,doctor_id))
    results = sql_query("SELECT * FROM student_doc")
    return render_template('student_doc.html', eresults=eresults, results=results, page="Students-Doctor Supervisors")

@app.route('/student_doc_edit2',methods = ['POST', 'GET']) #this is when user submits an edit
def student_doc_edit2():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'POST':
        old_roll_no = request.form['old_roll_no']
        old_doctor_id = request.form['old_doctor_id']
        roll_no = request.form['roll_no']
        doctor_id = request.form['doctor_id']
        term = request.form['term']
        field = request.form['field']
        dept_id = request.form['dept_id']
        eresults = sql_query('SELECT * FROM student_doc WHERE roll_no={} AND doctor_id={}'.format(roll_no,doctor_id))
        query = 'UPDATE student_doc set  roll_no = {},doctor_id = {},term = {},field = "{}",dept_id = {} WHERE roll_no = {} AND doctor_id = {}'.format(roll_no,doctor_id,term,field,dept_id,old_roll_no,old_doctor_id)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM student_doc')
    return render_template('student_doc.html', results=results, page="Students-Doctor Supervisors")

@app.route('/patient_fee')
def patient_fee():
    from functions.sqlquery import sql_query
    results = sql_query('SELECT * FROM patient_fee')
    return render_template('patient_fee.html', results=results, page="Patient Fees")

@app.route('/patient_fee_insert',methods = ['POST', 'GET']) #this is when user submits an insert
def patient_fee_insert():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    query=""
    if request.method == 'POST':
        patient_id = request.form['patient_id']
        amount_paid = request.form['amount_paid']
        amount_due = request.form['amount_due']
        query = 'INSERT INTO patient_fee VALUES ({},{},{})'.format(patient_id,amount_paid,amount_due)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM patient_fee')
    return render_template('patient_fee.html', results=results, page="Patient Fees")

@app.route('/patient_fee_delete',methods = ['POST', 'GET']) #this is when user clicks delete link
def patient_fee_delete():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'GET':
        patient_id = request.args.get('patient_id')
        query='DELETE FROM patient_fee WHERE patient_id={}'.format(patient_id)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM patient_fee')
    return render_template('patient_fee.html', results=results, page="Patient Fees")

@app.route('/patient_fee_edit1',methods = ['POST', 'GET']) #this is when user clicks edit link
def patient_fee_edit1():
    from functions.sqlquery import sql_query
    if request.method == 'GET':
        patient_id = request.args.get('patient_id')
        eresults = sql_query('SELECT * FROM patient_fee WHERE patient_id={}'.format(patient_id))
    results = sql_query("SELECT * FROM patient_fee")
    return render_template('patient_fee.html', eresults=eresults, results=results, page="Patient Fees")

@app.route('/patient_fee_edit2',methods = ['POST', 'GET']) #this is when user submits an edit
def patient_fee_edit2():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'POST':
        old_patient_id = request.form['old_patient_id']
        patient_id = request.form['patient_id']
        amount_paid = request.form['amount_paid']
        amount_due = request.form['amount_due']
        eresults = sql_query('SELECT * FROM patient_fee WHERE patient_id={}'.format(patient_id))
        query = 'UPDATE patient_fee set  patient_id = {},amount_paid = {},amount_due = {} WHERE patient_id = {}'.format(patient_id,amount_paid,amount_due,old_patient_id)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM patient_fee')
    return render_template('patient_fee.html', results=results, page="Patient Fees")

@app.route('/treatment')
def treatment():
    from functions.sqlquery import sql_query
    results = sql_query('SELECT * FROM treatment')
    return render_template('treatment.html', results=results, page="Patient History")

@app.route('/treatment_insert',methods = ['POST', 'GET']) #this is when user submits an insert
def treatment_insert():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    query=""
    if request.method == 'POST':
        patient_id = request.form['patient_id']
        doctor_id = request.form['doctor_id']
        date = request.form['date']
        date=date.split("-")
        date=int(date[2]+date[1]+date[0])
        time = request.form['time']
        temp = time.split(":")
        time=int(str(temp[0])+str(temp[1]))
        desc = request.form['desc']
        query = 'INSERT INTO treatment VALUES ({},{},{},{},"{}")'.format(patient_id,doctor_id,date,time,desc)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM treatment')
    return render_template('treatment.html', results=results, page="Patient History")

@app.route('/treatment_delete',methods = ['POST', 'GET']) #this is when user clicks delete link
def treatment_delete():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'GET':
        patient_id = request.args.get('patient_id')
        doctor_id = request.args.get('doctor_id')
        date = request.args.get('date')
        # date=date.split("-")
        # date=int(date[2]+date[1]+date[0])
        time = request.args.get('time')
        # temp = time.split(":")
        # time=int(str(temp[0])+str(temp[1]))
        query='DELETE FROM treatment WHERE patient_id={} AND doctor_id={} AND date={} AND time={}'.format(patient_id,doctor_id,date,time)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM treatment')
    return render_template('treatment.html', results=results, page="Patient History")

@app.route('/treatment_edit1',methods = ['POST', 'GET']) #this is when user clicks edit link
def treatment_edit1():
    from functions.sqlquery import sql_query
    if request.method == 'GET':
        patient_id = request.args.get('patient_id')
        doctor_id = request.args.get('doctor_id')
        date = request.args.get('date')
        # date=date.split("-")
        # date=int(date[2]+date[1]+date[0])
        time = request.args.get('time')
        # temp = time.split(":")
        # time=int(str(temp[0])+str(temp[1]))
        eresults = sql_query('SELECT * FROM treatment WHERE patient_id={} AND doctor_id={} AND date={} AND time={}'.format(patient_id,doctor_id,date,time))
    results = sql_query("SELECT * FROM treatment")
    return render_template('treatment.html', eresults=eresults, results=results, page="Patient History")

@app.route('/treatment_edit2',methods = ['POST', 'GET']) #this is when user submits an edit
def treatment_edit2():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'POST':
        old_patient_id = request.form['old_patient_id']
        old_doctor_id = request.form['old_doctor_id']
        old_date = request.form['old_date']
        # old_date=old_date.split("-")
        # old_date=int(old_date[2]+old_date[1]+old_date[0])
        old_time = request.form['old_time']
        # old_time = request.args.get('old_time')
        # temp = old_time.split(":")
        # old_time=int(str(temp[0])+str(temp[1]))
        patient_id = request.form['patient_id']
        doctor_id = request.form['doctor_id']
        date = request.form['date']
        date=date.split("-")
        date=int(date[2]+date[1]+date[0])
        time = request.form['time']
        temp = time.split(":")
        time=int(str(temp[0])+str(temp[1]))
        desc = request.form['desc']
        eresults = sql_query('SELECT * FROM treatment WHERE patient_id={} AND doctor_id={} AND date={} AND time={}'.format(patient_id,doctor_id,date,time))
        query = 'UPDATE treatment set  patient_id = {},doctor_id = {},date = {},time = {},desc = "{}" WHERE patient_id = {} AND doctor_id = {} AND date = {} AND time = {}'.format(patient_id,doctor_id,date,time,desc,old_patient_id,old_doctor_id,old_date,old_time)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM treatment')
    return render_template('treatment.html', results=results, page="Patient History")

@app.route('/transactions')
def transactions():
    from functions.sqlquery import sql_query
    results = sql_query('SELECT * FROM transactions')
    return render_template('transactions.html', results=results, page="Patient Transactions")

@app.route('/transactions_insert',methods = ['POST', 'GET']) #this is when user submits an insert
def transactions_insert():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    query=""
    if request.method == 'POST':
        price_list_id = request.form['price_list_id']
        patient_id = request.form['patient_id']
        quantity = request.form['quantity']
        query = 'INSERT INTO transactions VALUES ({},{},{})'.format(price_list_id,patient_id,quantity)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM transactions')
    return render_template('transactions.html', results=results, page="Patient Transactions")

@app.route('/transactions_delete',methods = ['POST', 'GET']) #this is when user clicks delete link
def transactions_delete():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'GET':
        price_list_id = request.args.get('price_list_id')
        query='DELETE FROM transactions WHERE price_list_id={}'.format(price_list_id)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM transactions')
    return render_template('transactions.html', results=results, page="Patient Transactions")

@app.route('/transactions_edit1',methods = ['POST', 'GET']) #this is when user clicks edit link
def transactions_edit1():
    from functions.sqlquery import sql_query
    if request.method == 'GET':
        price_list_id = request.args.get('price_list_id')
        eresults = sql_query('SELECT * FROM transactions WHERE price_list_id={}'.format(price_list_id))
    results = sql_query("SELECT * FROM transactions")
    return render_template('transactions.html', eresults=eresults, results=results, page="Patient Transactions")

@app.route('/transactions_edit2',methods = ['POST', 'GET']) #this is when user submits an edit
def transactions_edit2():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'POST':
        old_price_list_id = request.form['old_price_list_id']
        price_list_id = request.form['price_list_id']
        patient_id = request.form['patient_id']
        quantity = request.form['quantity']
        eresults = sql_query('SELECT * FROM transactions WHERE price_list_id={}'.format(price_list_id))
        query = 'UPDATE transactions set  price_list_id = {},patient_id = {},quantity = {} WHERE price_list_id = {}'.format(price_list_id,patient_id,quantity,old_price_list_id)
        sql_insert_edit_delete(query)
    results = sql_query('SELECT * FROM transactions')
    return render_template('transactions.html', results=results, page="Patient Transactions")

if __name__ == "__main__":
    app.run(debug=True)

