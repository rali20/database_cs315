@app.route('/patient_fee')
def patient_fee():
    from functions.sqlquery import sql_query
    results = sql_query('SELECT * FROM patient_fee')
    return render_template('patient_fee.html', results=results)

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
	return render_template('patient_fee.html', results=results)

@app.route('/patient_fee_delete',methods = ['POST', 'GET']) #this is when user clicks delete link
def patient_fee_delete():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'GET':
		patient_id = request.args.get('patient_id')
		query='DELETE FROM patient_fee WHERE patient_id={}'.format(patient_id)
		sql_insert_edit_delete(query)
	results = sql_query('SELECT * FROM patient_fee')
	return render_template('patient_fee.html', results=results)

@app.route('/patient_fee_edit1',methods = ['POST', 'GET']) #this is when user clicks edit link
def patient_fee_edit1():
    from functions.sqlquery import sql_query
    if request.method == 'GET':
		patient_id = request.args.get('patient_id')
		eresults = sql_query('SELECT * FROM patient_fee WHERE patient_id={}'.format(patient_id))
	results = sql_query("SELECT * FROM patient_fee")
	return render_template('patient_fee.html', eresults=eresults, results=results)

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
	return render_template('patient_fee.html', results=results)

