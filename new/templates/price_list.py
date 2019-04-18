@app.route('/price_list')
def price_list():
    from functions.sqlquery import sql_query
    results = sql_query('SELECT * FROM price_list')
    return render_template('price_list.html', results=results)

@app.route('/price_list_insert',methods = ['POST', 'GET']) #this is when user submits an insert
def price_list_insert():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    query=""
    if request.method == 'POST':
		price_list_id = request.form['price_list_id']
		category = request.form['category']
		price = request.form['price']
		desc = request.form['desc']
		query = 'INSERT INTO price_list VALUES ({},{},{},{})'.format(price_list_id,category,price,desc)
		sql_insert_edit_delete(query)
	results = sql_query('SELECT * FROM price_list')
	return render_template('price_list.html', results=results)

@app.route('/price_list_delete',methods = ['POST', 'GET']) #this is when user clicks delete link
def price_list_delete():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'GET':
		price_list_id = request.args.get('price_list_id')
		query='DELETE FROM price_list WHERE price_list_id={}'.format(price_list_id)
		sql_insert_edit_delete(query)
	results = sql_query('SELECT * FROM price_list')
	return render_template('price_list.html', results=results)

@app.route('/price_list_edit1',methods = ['POST', 'GET']) #this is when user clicks edit link
def price_list_edit1():
    from functions.sqlquery import sql_query
    if request.method == 'GET':
		price_list_id = request.args.get('price_list_id')
		eresults = sql_query('SELECT * FROM price_list WHERE price_list_id={}'.format(price_list_id))
	results = sql_query("SELECT * FROM price_list")
	return render_template('price_list.html', eresults=eresults, results=results)

@app.route('/price_list_edit2',methods = ['POST', 'GET']) #this is when user submits an edit
def price_list_edit2():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'POST':
		old_price_list_id = request.form['old_price_list_id']
		price_list_id = request.form['price_list_id']
		category = request.form['category']
		price = request.form['price']
		desc = request.form['desc']
		eresults = sql_query('SELECT * FROM price_list WHERE price_list_id={}'.format(price_list_id))
		query = 'UPDATE price_list set  price_list_id = {},category = {},price = {},desc = {} WHERE price_list_id = {}'.format(price_list_id,category,price,desc,old_price_list_id)
		sql_insert_edit_delete(query)
	results = sql_query('SELECT * FROM price_list')
	return render_template('price_list.html', results=results)

