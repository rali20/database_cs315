@app.route('/patients')
def patients():
    from functions.sqlquery import sql_query
    results = sql_query('SELECT * FROM patients')
    return render_template('patients.html', results=results)

@app.route('/patients_insert',methods = ['POST', 'GET']) #this is when user submits an insert
def patients_insert():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    query=""
    if request.method == 'POST':
		patient_id = request.form['patient_id']
		name = request.form['name']
		sex = request.form['sex']
		age = request.form['age']
		phone = request.form['phone']
		dob = request.form['dob']
		query = 'INSERT INTO patients VALUES ({},{},{},{},{},{})'.format(patient_id,name,sex,age,phone,dob)
		sql_insert_edit_delete(query)
	results = sql_query('SELECT * FROM patients')
	return render_template('patients.html', results=results)

@app.route('/patients_delete',methods = ['POST', 'GET']) #this is when user clicks delete link
def patients_delete():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'GET':
		patient_id = request.args.get('patient_id')
		query='DELETE FROM patients WHERE patient_id={}'.format(patient_id)
		sql_insert_edit_delete(query)
	results = sql_query('SELECT * FROM patients')
	return render_template('patients.html', results=results)

@app.route('/patients_edit1',methods = ['POST', 'GET']) #this is when user clicks edit link
def patients_edit1():
    from functions.sqlquery import sql_query
    if request.method == 'GET':
		patient_id = request.args.get('patient_id')
		eresults = sql_query('SELECT * FROM patients WHERE patient_id={}'.format(patient_id))
	results = sql_query("SELECT * FROM patients")
	return render_template('patients.html', eresults=eresults, results=results)

@app.route('/patients_edit2',methods = ['POST', 'GET']) #this is when user submits an edit
def patients_edit2():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'POST':
		old_patient_id = request.form['old_patient_id']
		patient_id = request.form['patient_id']
		name = request.form['name']
		sex = request.form['sex']
		age = request.form['age']
		phone = request.form['phone']
		dob = request.form['dob']
		eresults = sql_query('SELECT * FROM patients WHERE patient_id={}'.format(patient_id))
		query = 'UPDATE patients set  patient_id = {},name = {},sex = {},age = {},phone = {},dob = {} WHERE patient_id = {}'.format(patient_id,name,sex,age,phone,dob,old_patient_id)
		sql_insert_edit_delete(query)
	results = sql_query('SELECT * FROM patients')
	return render_template('patients.html', results=results)

