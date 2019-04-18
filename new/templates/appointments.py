@app.route('/appointments')
def appointments():
    from functions.sqlquery import sql_query
    results = sql_query('SELECT * FROM appointments')
    return render_template('appointments.html', results=results)

@app.route('/appointments_insert',methods = ['POST', 'GET']) #this is when user submits an insert
def appointments_insert():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    query=""
    if request.method == 'POST':
		doctor_id = request.form['doctor_id']
		patient_id = request.form['patient_id']
		date = request.form['date']
		time = request.form['time']
		description = request.form['description']
		query = 'INSERT INTO appointments VALUES ({},{},{},{},{})'.format(doctor_id,patient_id,date,time,description)
		sql_insert_edit_delete(query)
	results = sql_query('SELECT * FROM appointments')
	return render_template('appointments.html', results=results)

@app.route('/appointments_delete',methods = ['POST', 'GET']) #this is when user clicks delete link
def appointments_delete():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'GET':
		doctor_id = request.args.get('doctor_id')
		patient_id = request.args.get('patient_id')
		date = request.args.get('date')
		time = request.args.get('time')
		query='DELETE FROM appointments WHERE doctor_id={} AND patient_id={} AND date={} AND time={}'.format(doctor_id,patient_id,date,time)
		sql_insert_edit_delete(query)
	results = sql_query('SELECT * FROM appointments')
	return render_template('appointments.html', results=results)

@app.route('/appointments_edit1',methods = ['POST', 'GET']) #this is when user clicks edit link
def appointments_edit1():
    from functions.sqlquery import sql_query
    if request.method == 'GET':
		doctor_id = request.args.get('doctor_id')
		patient_id = request.args.get('patient_id')
		date = request.args.get('date')
		time = request.args.get('time')
		eresults = sql_query('SELECT * FROM appointments WHERE doctor_id={} AND patient_id={} AND date={} AND time={}'.format(doctor_id,patient_id,date,time))
	results = sql_query("SELECT * FROM appointments")
	return render_template('appointments.html', eresults=eresults, results=results)

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
		time = request.form['time']
		description = request.form['description']
		eresults = sql_query('SELECT * FROM appointments WHERE doctor_id={} AND patient_id={} AND date={} AND time={}'.format(doctor_id,patient_id,date,time))
		query = 'UPDATE appointments set  doctor_id = {},patient_id = {},date = {},time = {},description = {} WHERE doctor_id = {} AND patient_id = {} AND date = {} AND time = {}'.format(doctor_id,patient_id,date,time,description,old_doctor_id,old_patient_id,old_date,old_time)
		sql_insert_edit_delete(query)
	results = sql_query('SELECT * FROM appointments')
	return render_template('appointments.html', results=results)

