@app.route('/doctors')
def doctors():
    from functions.sqlquery import sql_query
    results = sql_query('SELECT * FROM doctors')
    return render_template('doctors.html', results=results)

@app.route('/doctors_insert',methods = ['POST', 'GET']) #this is when user submits an insert
def doctors_insert():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    query=""
    if request.method == 'POST':
		doctor_id = request.form['doctor_id']
		name = request.form['name']
		sex = request.form['sex']
		age = request.form['age']
		phone = request.form['phone']
		dob = request.form['dob']
		degree = request.form['degree']
		address = request.form['address']
		dept_id = request.form['dept_id']
		desg_id = request.form['desg_id']
		query = 'INSERT INTO doctors VALUES ({},{},{},{},{},{},{},{},{},{})'.format(doctor_id,name,sex,age,phone,dob,degree,address,dept_id,desg_id)
		sql_insert_edit_delete(query)
	results = sql_query('SELECT * FROM doctors')
	return render_template('doctors.html', results=results)

@app.route('/doctors_delete',methods = ['POST', 'GET']) #this is when user clicks delete link
def doctors_delete():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'GET':
		doctor_id = request.args.get('doctor_id')
		query='DELETE FROM doctors WHERE doctor_id={}'.format(doctor_id)
		sql_insert_edit_delete(query)
	results = sql_query('SELECT * FROM doctors')
	return render_template('doctors.html', results=results)

@app.route('/doctors_edit1',methods = ['POST', 'GET']) #this is when user clicks edit link
def doctors_edit1():
    from functions.sqlquery import sql_query
    if request.method == 'GET':
		doctor_id = request.args.get('doctor_id')
		eresults = sql_query('SELECT * FROM doctors WHERE doctor_id={}'.format(doctor_id))
	results = sql_query("SELECT * FROM doctors")
	return render_template('doctors.html', eresults=eresults, results=results)

@app.route('/doctors_edit2',methods = ['POST', 'GET']) #this is when user submits an edit
def doctors_edit2():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'POST':
		old_doctor_id = request.form['old_doctor_id']
		doctor_id = request.form['doctor_id']
		name = request.form['name']
		sex = request.form['sex']
		age = request.form['age']
		phone = request.form['phone']
		dob = request.form['dob']
		degree = request.form['degree']
		address = request.form['address']
		dept_id = request.form['dept_id']
		desg_id = request.form['desg_id']
		eresults = sql_query('SELECT * FROM doctors WHERE doctor_id={}'.format(doctor_id))
		query = 'UPDATE doctors set  doctor_id = {},name = {},sex = {},age = {},phone = {},dob = {},degree = {},address = {},dept_id = {},desg_id = {} WHERE doctor_id = {}'.format(doctor_id,name,sex,age,phone,dob,degree,address,dept_id,desg_id,old_doctor_id)
		sql_insert_edit_delete(query)
	results = sql_query('SELECT * FROM doctors')
	return render_template('doctors.html', results=results)

