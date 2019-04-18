@app.route('/desg')
def desg():
    from functions.sqlquery import sql_query
    results = sql_query('SELECT * FROM desg')
    return render_template('desg.html', results=results)

@app.route('/desg_insert',methods = ['POST', 'GET']) #this is when user submits an insert
def desg_insert():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    query=""
    if request.method == 'POST':
		desg_id = request.form['desg_id']
		name = request.form['name']
		salary = request.form['salary']
		dept_id = request.form['dept_id']
		query = 'INSERT INTO desg VALUES ({},{},{},{})'.format(desg_id,name,salary,dept_id)
		sql_insert_edit_delete(query)
	results = sql_query('SELECT * FROM desg')
	return render_template('desg.html', results=results)

@app.route('/desg_delete',methods = ['POST', 'GET']) #this is when user clicks delete link
def desg_delete():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'GET':
		desg_id = request.args.get('desg_id')
		query='DELETE FROM desg WHERE desg_id={}'.format(desg_id)
		sql_insert_edit_delete(query)
	results = sql_query('SELECT * FROM desg')
	return render_template('desg.html', results=results)

@app.route('/desg_edit1',methods = ['POST', 'GET']) #this is when user clicks edit link
def desg_edit1():
    from functions.sqlquery import sql_query
    if request.method == 'GET':
		desg_id = request.args.get('desg_id')
		eresults = sql_query('SELECT * FROM desg WHERE desg_id={}'.format(desg_id))
	results = sql_query("SELECT * FROM desg")
	return render_template('desg.html', eresults=eresults, results=results)

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
		query = 'UPDATE desg set  desg_id = {},name = {},salary = {},dept_id = {} WHERE desg_id = {}'.format(desg_id,name,salary,dept_id,old_desg_id)
		sql_insert_edit_delete(query)
	results = sql_query('SELECT * FROM desg')
	return render_template('desg.html', results=results)

