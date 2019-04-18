@app.route('/visiting')
def visiting():
    from functions.sqlquery import sql_query
    results = sql_query('SELECT * FROM visiting')
    return render_template('visiting.html', results=results)

@app.route('/visiting_insert',methods = ['POST', 'GET']) #this is when user submits an insert
def visiting_insert():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    query=""
    if request.method == 'POST':
		time_in = request.form['time_in']
		time_out = request.form['time_out']
		patient_id = request.form['patient_id']
		visitor_id = request.form['visitor_id']
		query = 'INSERT INTO visiting VALUES ({},{},{},{})'.format(time_in,time_out,patient_id,visitor_id)
		sql_insert_edit_delete(query)
	results = sql_query('SELECT * FROM visiting')
	return render_template('visiting.html', results=results)

@app.route('/visiting_delete',methods = ['POST', 'GET']) #this is when user clicks delete link
def visiting_delete():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'GET':
		time_in = request.args.get('time_in')
		time_out = request.args.get('time_out')
		patient_id = request.args.get('patient_id')
		visitor_id = request.args.get('visitor_id')
		query='DELETE FROM visiting WHERE time_in={} AND time_out={} AND patient_id={} AND visitor_id={}'.format(time_in,time_out,patient_id,visitor_id)
		sql_insert_edit_delete(query)
	results = sql_query('SELECT * FROM visiting')
	return render_template('visiting.html', results=results)

@app.route('/visiting_edit1',methods = ['POST', 'GET']) #this is when user clicks edit link
def visiting_edit1():
    from functions.sqlquery import sql_query
    if request.method == 'GET':
		time_in = request.args.get('time_in')
		time_out = request.args.get('time_out')
		patient_id = request.args.get('patient_id')
		visitor_id = request.args.get('visitor_id')
		eresults = sql_query('SELECT * FROM visiting WHERE time_in={} AND time_out={} AND patient_id={} AND visitor_id={}'.format(time_in,time_out,patient_id,visitor_id))
	results = sql_query("SELECT * FROM visiting")
	return render_template('visiting.html', eresults=eresults, results=results)

@app.route('/visiting_edit2',methods = ['POST', 'GET']) #this is when user submits an edit
def visiting_edit2():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'POST':
		old_time_in = request.form['old_time_in']
		old_time_out = request.form['old_time_out']
		old_patient_id = request.form['old_patient_id']
		old_visitor_id = request.form['old_visitor_id']
		time_in = request.form['time_in']
		time_out = request.form['time_out']
		patient_id = request.form['patient_id']
		visitor_id = request.form['visitor_id']
		eresults = sql_query('SELECT * FROM visiting WHERE time_in={} AND time_out={} AND patient_id={} AND visitor_id={}'.format(time_in,time_out,patient_id,visitor_id))
		query = 'UPDATE visiting set  time_in = {},time_out = {},patient_id = {},visitor_id = {} WHERE time_in = {} AND time_out = {} AND patient_id = {} AND visitor_id = {}'.format(time_in,time_out,patient_id,visitor_id,old_time_in,old_time_out,old_patient_id,old_visitor_id)
		sql_insert_edit_delete(query)
	results = sql_query('SELECT * FROM visiting')
	return render_template('visiting.html', results=results)

