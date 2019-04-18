@app.route('/visitor')
def visitor():
    from functions.sqlquery import sql_query
    results = sql_query('SELECT * FROM visitor')
    return render_template('visitor.html', results=results)

@app.route('/visitor_insert',methods = ['POST', 'GET']) #this is when user submits an insert
def visitor_insert():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    query=""
    if request.method == 'POST':
		visitor_id = request.form['visitor_id']
		name = request.form['name']
		phone = request.form['phone']
		sex = request.form['sex']
		age = request.form['age']
		query = 'INSERT INTO visitor VALUES ({},{},{},{},{})'.format(visitor_id,name,phone,sex,age)
		sql_insert_edit_delete(query)
	results = sql_query('SELECT * FROM visitor')
	return render_template('visitor.html', results=results)

@app.route('/visitor_delete',methods = ['POST', 'GET']) #this is when user clicks delete link
def visitor_delete():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'GET':
		visitor_id = request.args.get('visitor_id')
		query='DELETE FROM visitor WHERE visitor_id={}'.format(visitor_id)
		sql_insert_edit_delete(query)
	results = sql_query('SELECT * FROM visitor')
	return render_template('visitor.html', results=results)

@app.route('/visitor_edit1',methods = ['POST', 'GET']) #this is when user clicks edit link
def visitor_edit1():
    from functions.sqlquery import sql_query
    if request.method == 'GET':
		visitor_id = request.args.get('visitor_id')
		eresults = sql_query('SELECT * FROM visitor WHERE visitor_id={}'.format(visitor_id))
	results = sql_query("SELECT * FROM visitor")
	return render_template('visitor.html', eresults=eresults, results=results)

@app.route('/visitor_edit2',methods = ['POST', 'GET']) #this is when user submits an edit
def visitor_edit2():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'POST':
		old_visitor_id = request.form['old_visitor_id']
		visitor_id = request.form['visitor_id']
		name = request.form['name']
		phone = request.form['phone']
		sex = request.form['sex']
		age = request.form['age']
		eresults = sql_query('SELECT * FROM visitor WHERE visitor_id={}'.format(visitor_id))
		query = 'UPDATE visitor set  visitor_id = {},name = {},phone = {},sex = {},age = {} WHERE visitor_id = {}'.format(visitor_id,name,phone,sex,age,old_visitor_id)
		sql_insert_edit_delete(query)
	results = sql_query('SELECT * FROM visitor')
	return render_template('visitor.html', results=results)

