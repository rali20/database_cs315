@app.route('/inventory')
def inventory():
    from functions.sqlquery import sql_query
    results = sql_query('SELECT * FROM inventory')
    return render_template('inventory.html', results=results)

@app.route('/inventory_insert',methods = ['POST', 'GET']) #this is when user submits an insert
def inventory_insert():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    query=""
    if request.method == 'POST':
		equip_id = request.form['equip_id']
		dept_id = request.form['dept_id']
		name = request.form['name']
		quantity = request.form['quantity']
		query = 'INSERT INTO inventory VALUES ({},{},{},{})'.format(equip_id,dept_id,name,quantity)
		sql_insert_edit_delete(query)
	results = sql_query('SELECT * FROM inventory')
	return render_template('inventory.html', results=results)

@app.route('/inventory_delete',methods = ['POST', 'GET']) #this is when user clicks delete link
def inventory_delete():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'GET':
		equip_id = request.args.get('equip_id')
		dept_id = request.args.get('dept_id')
		query='DELETE FROM inventory WHERE equip_id={} AND dept_id={}'.format(equip_id,dept_id)
		sql_insert_edit_delete(query)
	results = sql_query('SELECT * FROM inventory')
	return render_template('inventory.html', results=results)

@app.route('/inventory_edit1',methods = ['POST', 'GET']) #this is when user clicks edit link
def inventory_edit1():
    from functions.sqlquery import sql_query
    if request.method == 'GET':
		equip_id = request.args.get('equip_id')
		dept_id = request.args.get('dept_id')
		eresults = sql_query('SELECT * FROM inventory WHERE equip_id={} AND dept_id={}'.format(equip_id,dept_id))
	results = sql_query("SELECT * FROM inventory")
	return render_template('inventory.html', eresults=eresults, results=results)

@app.route('/inventory_edit2',methods = ['POST', 'GET']) #this is when user submits an edit
def inventory_edit2():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'POST':
		old_equip_id = request.form['old_equip_id']
		old_dept_id = request.form['old_dept_id']
		equip_id = request.form['equip_id']
		dept_id = request.form['dept_id']
		name = request.form['name']
		quantity = request.form['quantity']
		eresults = sql_query('SELECT * FROM inventory WHERE equip_id={} AND dept_id={}'.format(equip_id,dept_id))
		query = 'UPDATE inventory set  equip_id = {},dept_id = {},name = {},quantity = {} WHERE equip_id = {} AND dept_id = {}'.format(equip_id,dept_id,name,quantity,old_equip_id,old_dept_id)
		sql_insert_edit_delete(query)
	results = sql_query('SELECT * FROM inventory')
	return render_template('inventory.html', results=results)

