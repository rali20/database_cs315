@app.route('/transactions')
def transactions():
    from functions.sqlquery import sql_query
    results = sql_query('SELECT * FROM transactions')
    return render_template('transactions.html', results=results)

@app.route('/transactions_insert',methods = ['POST', 'GET']) #this is when user submits an insert
def transactions_insert():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    query=""
    if request.method == 'POST':
		price_list_id = request.form['price_list_id']
		patient_id = request.form['patient_id']
		quantity = request.form['quantity']
		query = 'INSERT INTO transactions VALUES ({},{},{})'.format(price_list_id,patient_id,quantity)
		sql_insert_edit_delete(query)
	results = sql_query('SELECT * FROM transactions')
	return render_template('transactions.html', results=results)

@app.route('/transactions_delete',methods = ['POST', 'GET']) #this is when user clicks delete link
def transactions_delete():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'GET':
		price_list_id = request.args.get('price_list_id')
		query='DELETE FROM transactions WHERE price_list_id={}'.format(price_list_id)
		sql_insert_edit_delete(query)
	results = sql_query('SELECT * FROM transactions')
	return render_template('transactions.html', results=results)

@app.route('/transactions_edit1',methods = ['POST', 'GET']) #this is when user clicks edit link
def transactions_edit1():
    from functions.sqlquery import sql_query
    if request.method == 'GET':
		price_list_id = request.args.get('price_list_id')
		eresults = sql_query('SELECT * FROM transactions WHERE price_list_id={}'.format(price_list_id))
	results = sql_query("SELECT * FROM transactions")
	return render_template('transactions.html', eresults=eresults, results=results)

@app.route('/transactions_edit2',methods = ['POST', 'GET']) #this is when user submits an edit
def transactions_edit2():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'POST':
		old_price_list_id = request.form['old_price_list_id']
		price_list_id = request.form['price_list_id']
		patient_id = request.form['patient_id']
		quantity = request.form['quantity']
		eresults = sql_query('SELECT * FROM transactions WHERE price_list_id={}'.format(price_list_id))
		query = 'UPDATE transactions set  price_list_id = {},patient_id = {},quantity = {} WHERE price_list_id = {}'.format(price_list_id,patient_id,quantity,old_price_list_id)
		sql_insert_edit_delete(query)
	results = sql_query('SELECT * FROM transactions')
	return render_template('transactions.html', results=results)

