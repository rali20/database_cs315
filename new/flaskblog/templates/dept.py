@app.route('/dept')
def dept():
    from functions.sqlquery import sql_query
    results = sql_query('SELECT * FROM dept')
    return render_template('dept.html', results=results)

@app.route('/dept_insert',methods = ['POST', 'GET']) #this is when user submits an insert
def dept_insert():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    query=""
    if request.method == 'POST':
		dept_id = request.form['dept_id']
		name = request.form['name']
		doctor_id = request.form['doctor_id']
		query = 'INSERT INTO dept VALUES ({},{},{})'.format(dept_id,name,doctor_id)
		sql_insert_edit_delete(query)
	results = sql_query('SELECT * FROM dept')
	return render_template('dept.html', results=results)

@app.route('/dept_delete',methods = ['POST', 'GET']) #this is when user clicks delete link
def dept_delete():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'GET':
		dept_id = request.args.get('dept_id')
		query='DELETE FROM dept WHERE dept_id={}'.format(dept_id)
		sql_insert_edit_delete(query)
	results = sql_query('SELECT * FROM dept')
	return render_template('dept.html', results=results)

@app.route('/dept_edit1',methods = ['POST', 'GET']) #this is when user clicks edit link
def dept_edit1():
    from functions.sqlquery import sql_query
    if request.method == 'GET':
		dept_id = request.args.get('dept_id')
		eresults = sql_query('SELECT * FROM dept WHERE dept_id={}'.format(dept_id))
	results = sql_query("SELECT * FROM dept")
	return render_template('dept.html', eresults=eresults, results=results)

@app.route('/dept_edit2',methods = ['POST', 'GET']) #this is when user submits an edit
def dept_edit2():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'POST':
		old_dept_id = request.form['old_dept_id']
		dept_id = request.form['dept_id']
		name = request.form['name']
		doctor_id = request.form['doctor_id']
		eresults = sql_query('SELECT * FROM dept WHERE dept_id={}'.format(dept_id))
		query = 'UPDATE dept set  dept_id = {},name = {},doctor_id = {} WHERE dept_id = {}'.format(dept_id,name,doctor_id,old_dept_id)
		sql_insert_edit_delete(query)
	results = sql_query('SELECT * FROM dept')
	return render_template('dept.html', results=results)

