@app.route('/treatment')
def treatment():
    from functions.sqlquery import sql_query
    results = sql_query('SELECT * FROM treatment')
    return render_template('treatment.html', results=results)

@app.route('/treatment_insert',methods = ['POST', 'GET']) #this is when user submits an insert
def treatment_insert():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    query=""
    if request.method == 'POST':
		patient_id = request.form['patient_id']
		doctor_id = request.form['doctor_id']
		date = request.form['date']
		time = request.form['time']
		desc = request.form['desc']
		query = 'INSERT INTO treatment VALUES ({},{},{},{},{})'.format(patient_id,doctor_id,date,time,desc)
		sql_insert_edit_delete(query)
	results = sql_query('SELECT * FROM treatment')
	return render_template('treatment.html', results=results)

@app.route('/treatment_delete',methods = ['POST', 'GET']) #this is when user clicks delete link
def treatment_delete():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'GET':
		patient_id = request.args.get('patient_id')
		doctor_id = request.args.get('doctor_id')
		date = request.args.get('date')
		time = request.args.get('time')
		query='DELETE FROM treatment WHERE patient_id={} AND doctor_id={} AND date={} AND time={}'.format(patient_id,doctor_id,date,time)
		sql_insert_edit_delete(query)
	results = sql_query('SELECT * FROM treatment')
	return render_template('treatment.html', results=results)

@app.route('/treatment_edit1',methods = ['POST', 'GET']) #this is when user clicks edit link
def treatment_edit1():
    from functions.sqlquery import sql_query
    if request.method == 'GET':
		patient_id = request.args.get('patient_id')
		doctor_id = request.args.get('doctor_id')
		date = request.args.get('date')
		time = request.args.get('time')
		eresults = sql_query('SELECT * FROM treatment WHERE patient_id={} AND doctor_id={} AND date={} AND time={}'.format(patient_id,doctor_id,date,time))
	results = sql_query("SELECT * FROM treatment")
	return render_template('treatment.html', eresults=eresults, results=results)

@app.route('/treatment_edit2',methods = ['POST', 'GET']) #this is when user submits an edit
def treatment_edit2():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'POST':
		old_patient_id = request.form['old_patient_id']
		old_doctor_id = request.form['old_doctor_id']
		old_date = request.form['old_date']
		old_time = request.form['old_time']
		patient_id = request.form['patient_id']
		doctor_id = request.form['doctor_id']
		date = request.form['date']
		time = request.form['time']
		desc = request.form['desc']
		eresults = sql_query('SELECT * FROM treatment WHERE patient_id={} AND doctor_id={} AND date={} AND time={}'.format(patient_id,doctor_id,date,time))
		query = 'UPDATE treatment set  patient_id = {},doctor_id = {},date = {},time = {},desc = {} WHERE patient_id = {} AND doctor_id = {} AND date = {} AND time = {}'.format(patient_id,doctor_id,date,time,desc,old_patient_id,old_doctor_id,old_date,old_time)
		sql_insert_edit_delete(query)
	results = sql_query('SELECT * FROM treatment')
	return render_template('treatment.html', results=results)

