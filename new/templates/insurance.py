@app.route('/insurance')
def insurance():
    from functions.sqlquery import sql_query
    results = sql_query('SELECT * FROM insurance')
    return render_template('insurance.html', results=results)

@app.route('/insurance_insert',methods = ['POST', 'GET']) #this is when user submits an insert
def insurance_insert():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    query=""
    if request.method == 'POST':
		insurance_id = request.form['insurance_id']
		name = request.form['name']
		company_name = request.form['company_name']
		amount = request.form['amount']
		receiver_id = request.form['receiver_id']
		receiver_name = request.form['receiver_name']
		query = 'INSERT INTO insurance VALUES ({},{},{},{},{},{})'.format(insurance_id,name,company_name,amount,receiver_id,receiver_name)
		sql_insert_edit_delete(query)
	results = sql_query('SELECT * FROM insurance')
	return render_template('insurance.html', results=results)

@app.route('/insurance_delete',methods = ['POST', 'GET']) #this is when user clicks delete link
def insurance_delete():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'GET':
		insurance_id = request.args.get('insurance_id')
		query='DELETE FROM insurance WHERE insurance_id={}'.format(insurance_id)
		sql_insert_edit_delete(query)
	results = sql_query('SELECT * FROM insurance')
	return render_template('insurance.html', results=results)

@app.route('/insurance_edit1',methods = ['POST', 'GET']) #this is when user clicks edit link
def insurance_edit1():
    from functions.sqlquery import sql_query
    if request.method == 'GET':
		insurance_id = request.args.get('insurance_id')
		eresults = sql_query('SELECT * FROM insurance WHERE insurance_id={}'.format(insurance_id))
	results = sql_query("SELECT * FROM insurance")
	return render_template('insurance.html', eresults=eresults, results=results)

@app.route('/insurance_edit2',methods = ['POST', 'GET']) #this is when user submits an edit
def insurance_edit2():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'POST':
		old_insurance_id = request.form['old_insurance_id']
		insurance_id = request.form['insurance_id']
		name = request.form['name']
		company_name = request.form['company_name']
		amount = request.form['amount']
		receiver_id = request.form['receiver_id']
		receiver_name = request.form['receiver_name']
		eresults = sql_query('SELECT * FROM insurance WHERE insurance_id={}'.format(insurance_id))
		query = 'UPDATE insurance set  insurance_id = {},name = {},company_name = {},amount = {},receiver_id = {},receiver_name = {} WHERE insurance_id = {}'.format(insurance_id,name,company_name,amount,receiver_id,receiver_name,old_insurance_id)
		sql_insert_edit_delete(query)
	results = sql_query('SELECT * FROM insurance')
	return render_template('insurance.html', results=results)

