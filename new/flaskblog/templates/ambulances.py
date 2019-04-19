@app.route('/ambulances')
def ambulances():
    from functions.sqlquery import sql_query
    results = sql_query('SELECT * FROM ambulances')
    return render_template('ambulances.html', results=results)

@app.route('/ambulances_insert',methods = ['POST', 'GET']) #this is when user submits an insert
def ambulances_insert():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    query=""
    if request.method == 'POST':
		vehicle_no = request.form['vehicle_no']
		emp_id = request.form['emp_id']
		model_name = request.form['model_name']
		type = request.form['type']
		query = 'INSERT INTO ambulances VALUES ({},{},{},{})'.format(vehicle_no,emp_id,model_name,type)
		sql_insert_edit_delete(query)
	results = sql_query('SELECT * FROM ambulances')
	return render_template('ambulances.html', results=results)

@app.route('/ambulances_delete',methods = ['POST', 'GET']) #this is when user clicks delete link
def ambulances_delete():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'GET':
		vehicle_no = request.args.get('vehicle_no')
		emp_id = request.args.get('emp_id')
		query='DELETE FROM ambulances WHERE vehicle_no={} AND emp_id={}'.format(vehicle_no,emp_id)
		sql_insert_edit_delete(query)
	results = sql_query('SELECT * FROM ambulances')
	return render_template('ambulances.html', results=results)

@app.route('/ambulances_edit1',methods = ['POST', 'GET']) #this is when user clicks edit link
def ambulances_edit1():
    from functions.sqlquery import sql_query
    if request.method == 'GET':
		vehicle_no = request.args.get('vehicle_no')
		emp_id = request.args.get('emp_id')
		eresults = sql_query('SELECT * FROM ambulances WHERE vehicle_no={} AND emp_id={}'.format(vehicle_no,emp_id))
	results = sql_query("SELECT * FROM ambulances")
	return render_template('ambulances.html', eresults=eresults, results=results)

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
		query = 'UPDATE ambulances set  vehicle_no = {},emp_id = {},model_name = {},type = {} WHERE vehicle_no = {} AND emp_id = {}'.format(vehicle_no,emp_id,model_name,type,old_vehicle_no,old_emp_id)
		sql_insert_edit_delete(query)
	results = sql_query('SELECT * FROM ambulances')
	return render_template('ambulances.html', results=results)

