@app.route('/employee')
def employee():
    from functions.sqlquery import sql_query
    results = sql_query('SELECT * FROM employee')
    return render_template('employee.html', results=results)

@app.route('/employee_insert',methods = ['POST', 'GET']) #this is when user submits an insert
def employee_insert():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    query=""
    if request.method == 'POST':
		emp_id = request.form['emp_id']
		name = request.form['name']
		sex = request.form['sex']
		age = request.form['age']
		phone = request.form['phone']
		dob = request.form['dob']
		address = request.form['address']
		dept_id = request.form['dept_id']
		desg_id = request.form['desg_id']
		query = 'INSERT INTO employee VALUES ({},{},{},{},{},{},{},{},{})'.format(emp_id,name,sex,age,phone,dob,address,dept_id,desg_id)
		sql_insert_edit_delete(query)
	results = sql_query('SELECT * FROM employee')
	return render_template('employee.html', results=results)

@app.route('/employee_delete',methods = ['POST', 'GET']) #this is when user clicks delete link
def employee_delete():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'GET':
		emp_id = request.args.get('emp_id')
		query='DELETE FROM employee WHERE emp_id={}'.format(emp_id)
		sql_insert_edit_delete(query)
	results = sql_query('SELECT * FROM employee')
	return render_template('employee.html', results=results)

@app.route('/employee_edit1',methods = ['POST', 'GET']) #this is when user clicks edit link
def employee_edit1():
    from functions.sqlquery import sql_query
    if request.method == 'GET':
		emp_id = request.args.get('emp_id')
		eresults = sql_query('SELECT * FROM employee WHERE emp_id={}'.format(emp_id))
	results = sql_query("SELECT * FROM employee")
	return render_template('employee.html', eresults=eresults, results=results)

@app.route('/employee_edit2',methods = ['POST', 'GET']) #this is when user submits an edit
def employee_edit2():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'POST':
		old_emp_id = request.form['old_emp_id']
		emp_id = request.form['emp_id']
		name = request.form['name']
		sex = request.form['sex']
		age = request.form['age']
		phone = request.form['phone']
		dob = request.form['dob']
		address = request.form['address']
		dept_id = request.form['dept_id']
		desg_id = request.form['desg_id']
		eresults = sql_query('SELECT * FROM employee WHERE emp_id={}'.format(emp_id))
		query = 'UPDATE employee set  emp_id = {},name = {},sex = {},age = {},phone = {},dob = {},address = {},dept_id = {},desg_id = {} WHERE emp_id = {}'.format(emp_id,name,sex,age,phone,dob,address,dept_id,desg_id,old_emp_id)
		sql_insert_edit_delete(query)
	results = sql_query('SELECT * FROM employee')
	return render_template('employee.html', results=results)

