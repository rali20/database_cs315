@app.route('/students')
def students():
    from functions.sqlquery import sql_query
    results = sql_query('SELECT * FROM students')
    return render_template('students.html', results=results)

@app.route('/students_insert',methods = ['POST', 'GET']) #this is when user submits an insert
def students_insert():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    query=""
    if request.method == 'POST':
		roll_no = request.form['roll_no']
		name = request.form['name']
		degree = request.form['degree']
		year = request.form['year']
		sex = request.form['sex']
		phone = request.form['phone']
		dob = request.form['dob']
		address = request.form['address']
		query = 'INSERT INTO students VALUES ({},{},{},{},{},{},{},{})'.format(roll_no,name,degree,year,sex,phone,dob,address)
		sql_insert_edit_delete(query)
	results = sql_query('SELECT * FROM students')
	return render_template('students.html', results=results)

@app.route('/students_delete',methods = ['POST', 'GET']) #this is when user clicks delete link
def students_delete():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'GET':
		visitor_id = request.args.get('visitor_id')
		query='DELETE FROM students WHERE visitor_id={}'.format(visitor_id)
		sql_insert_edit_delete(query)
	results = sql_query('SELECT * FROM students')
	return render_template('students.html', results=results)

@app.route('/students_edit1',methods = ['POST', 'GET']) #this is when user clicks edit link
def students_edit1():
    from functions.sqlquery import sql_query
    if request.method == 'GET':
		visitor_id = request.args.get('visitor_id')
		eresults = sql_query('SELECT * FROM students WHERE visitor_id={}'.format(visitor_id))
	results = sql_query("SELECT * FROM students")
	return render_template('students.html', eresults=eresults, results=results)

@app.route('/students_edit2',methods = ['POST', 'GET']) #this is when user submits an edit
def students_edit2():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'POST':
		old_visitor_id = request.form['old_visitor_id']
		roll_no = request.form['roll_no']
		name = request.form['name']
		degree = request.form['degree']
		year = request.form['year']
		sex = request.form['sex']
		phone = request.form['phone']
		dob = request.form['dob']
		address = request.form['address']
		eresults = sql_query('SELECT * FROM students WHERE visitor_id={}'.format(visitor_id))
		query = 'UPDATE students set  roll_no = {},name = {},degree = {},year = {},sex = {},phone = {},dob = {},address = {} WHERE visitor_id = {}'.format(roll_no,name,degree,year,sex,phone,dob,address,old_visitor_id)
		sql_insert_edit_delete(query)
	results = sql_query('SELECT * FROM students')
	return render_template('students.html', results=results)

