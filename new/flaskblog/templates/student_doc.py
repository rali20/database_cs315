@app.route('/student_doc')
def student_doc():
    from functions.sqlquery import sql_query
    results = sql_query('SELECT * FROM student_doc')
    return render_template('student_doc.html', results=results)

@app.route('/student_doc_insert',methods = ['POST', 'GET']) #this is when user submits an insert
def student_doc_insert():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    query=""
    if request.method == 'POST':
		roll_no = request.form['roll_no']
		doctor_id = request.form['doctor_id']
		term = request.form['term']
		field = request.form['field']
		dept_id = request.form['dept_id']
		query = 'INSERT INTO student_doc VALUES ({},{},{},{},{})'.format(roll_no,doctor_id,term,field,dept_id)
		sql_insert_edit_delete(query)
	results = sql_query('SELECT * FROM student_doc')
	return render_template('student_doc.html', results=results)

@app.route('/student_doc_delete',methods = ['POST', 'GET']) #this is when user clicks delete link
def student_doc_delete():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'GET':
		roll_no = request.args.get('roll_no')
		doctor_id = request.args.get('doctor_id')
		query='DELETE FROM student_doc WHERE roll_no={} AND doctor_id={}'.format(roll_no,doctor_id)
		sql_insert_edit_delete(query)
	results = sql_query('SELECT * FROM student_doc')
	return render_template('student_doc.html', results=results)

@app.route('/student_doc_edit1',methods = ['POST', 'GET']) #this is when user clicks edit link
def student_doc_edit1():
    from functions.sqlquery import sql_query
    if request.method == 'GET':
		roll_no = request.args.get('roll_no')
		doctor_id = request.args.get('doctor_id')
		eresults = sql_query('SELECT * FROM student_doc WHERE roll_no={} AND doctor_id={}'.format(roll_no,doctor_id))
	results = sql_query("SELECT * FROM student_doc")
	return render_template('student_doc.html', eresults=eresults, results=results)

@app.route('/student_doc_edit2',methods = ['POST', 'GET']) #this is when user submits an edit
def student_doc_edit2():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'POST':
		old_roll_no = request.form['old_roll_no']
		old_doctor_id = request.form['old_doctor_id']
		roll_no = request.form['roll_no']
		doctor_id = request.form['doctor_id']
		term = request.form['term']
		field = request.form['field']
		dept_id = request.form['dept_id']
		eresults = sql_query('SELECT * FROM student_doc WHERE roll_no={} AND doctor_id={}'.format(roll_no,doctor_id))
		query = 'UPDATE student_doc set  roll_no = {},doctor_id = {},term = {},field = {},dept_id = {} WHERE roll_no = {} AND doctor_id = {}'.format(roll_no,doctor_id,term,field,dept_id,old_roll_no,old_doctor_id)
		sql_insert_edit_delete(query)
	results = sql_query('SELECT * FROM student_doc')
	return render_template('student_doc.html', results=results)

