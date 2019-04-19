@app.route('/lib_issued')
def lib_issued():
    from functions.sqlquery import sql_query
    results = sql_query('SELECT * FROM lib_issued')
    return render_template('lib_issued.html', results=results)

@app.route('/lib_issued_insert',methods = ['POST', 'GET']) #this is when user submits an insert
def lib_issued_insert():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    query=""
    if request.method == 'POST':
		issue_date = request.form['issue_date']
		book_id = request.form['book_id']
		return_status = request.form['return_status']
		return_date = request.form['return_date']
		doctor_id = request.form['doctor_id']
		roll_no = request.form['roll_no']
		emp_id = request.form['emp_id']
		query = 'INSERT INTO lib_issued VALUES ({},{},{},{},{},{},{})'.format(issue_date,book_id,return_status,return_date,doctor_id,roll_no,emp_id)
		sql_insert_edit_delete(query)
	results = sql_query('SELECT * FROM lib_issued')
	return render_template('lib_issued.html', results=results)

@app.route('/lib_issued_delete',methods = ['POST', 'GET']) #this is when user clicks delete link
def lib_issued_delete():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'GET':
		issue_date = request.args.get('issue_date')
		book_id = request.args.get('book_id')
		query='DELETE FROM lib_issued WHERE issue_date={} AND book_id={}'.format(issue_date,book_id)
		sql_insert_edit_delete(query)
	results = sql_query('SELECT * FROM lib_issued')
	return render_template('lib_issued.html', results=results)

@app.route('/lib_issued_edit1',methods = ['POST', 'GET']) #this is when user clicks edit link
def lib_issued_edit1():
    from functions.sqlquery import sql_query
    if request.method == 'GET':
		issue_date = request.args.get('issue_date')
		book_id = request.args.get('book_id')
		eresults = sql_query('SELECT * FROM lib_issued WHERE issue_date={} AND book_id={}'.format(issue_date,book_id))
	results = sql_query("SELECT * FROM lib_issued")
	return render_template('lib_issued.html', eresults=eresults, results=results)

@app.route('/lib_issued_edit2',methods = ['POST', 'GET']) #this is when user submits an edit
def lib_issued_edit2():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'POST':
		old_issue_date = request.form['old_issue_date']
		old_book_id = request.form['old_book_id']
		issue_date = request.form['issue_date']
		book_id = request.form['book_id']
		return_status = request.form['return_status']
		return_date = request.form['return_date']
		doctor_id = request.form['doctor_id']
		roll_no = request.form['roll_no']
		emp_id = request.form['emp_id']
		eresults = sql_query('SELECT * FROM lib_issued WHERE issue_date={} AND book_id={}'.format(issue_date,book_id))
		query = 'UPDATE lib_issued set  issue_date = {},book_id = {},return_status = {},return_date = {},doctor_id = {},roll_no = {},emp_id = {} WHERE issue_date = {} AND book_id = {}'.format(issue_date,book_id,return_status,return_date,doctor_id,roll_no,emp_id,old_issue_date,old_book_id)
		sql_insert_edit_delete(query)
	results = sql_query('SELECT * FROM lib_issued')
	return render_template('lib_issued.html', results=results)

