@app.route('/vendors')
def vendors():
    from functions.sqlquery import sql_query
    results = sql_query('SELECT * FROM vendors')
    return render_template('vendors.html', results=results)

@app.route('/vendors_insert',methods = ['POST', 'GET']) #this is when user submits an insert
def vendors_insert():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    query=""
    if request.method == 'POST':
		vendor_id = request.form['vendor_id']
		name = request.form['name']
		phone = request.form['phone']
		query = 'INSERT INTO vendors VALUES ({},{},{})'.format(vendor_id,name,phone)
		sql_insert_edit_delete(query)
	results = sql_query('SELECT * FROM vendors')
	return render_template('vendors.html', results=results)

@app.route('/vendors_delete',methods = ['POST', 'GET']) #this is when user clicks delete link
def vendors_delete():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'GET':
		vendor_id = request.args.get('vendor_id')
		query='DELETE FROM vendors WHERE vendor_id={}'.format(vendor_id)
		sql_insert_edit_delete(query)
	results = sql_query('SELECT * FROM vendors')
	return render_template('vendors.html', results=results)

@app.route('/vendors_edit1',methods = ['POST', 'GET']) #this is when user clicks edit link
def vendors_edit1():
    from functions.sqlquery import sql_query
    if request.method == 'GET':
		vendor_id = request.args.get('vendor_id')
		eresults = sql_query('SELECT * FROM vendors WHERE vendor_id={}'.format(vendor_id))
	results = sql_query("SELECT * FROM vendors")
	return render_template('vendors.html', eresults=eresults, results=results)

@app.route('/vendors_edit2',methods = ['POST', 'GET']) #this is when user submits an edit
def vendors_edit2():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'POST':
		old_vendor_id = request.form['old_vendor_id']
		vendor_id = request.form['vendor_id']
		name = request.form['name']
		phone = request.form['phone']
		eresults = sql_query('SELECT * FROM vendors WHERE vendor_id={}'.format(vendor_id))
		query = 'UPDATE vendors set  vendor_id = {},name = {},phone = {} WHERE vendor_id = {}'.format(vendor_id,name,phone,old_vendor_id)
		sql_insert_edit_delete(query)
	results = sql_query('SELECT * FROM vendors')
	return render_template('vendors.html', results=results)

