@app.route('/library')
def library():
    from functions.sqlquery import sql_query
    results = sql_query('SELECT * FROM library')
    return render_template('library.html', results=results)

@app.route('/library_insert',methods = ['POST', 'GET']) #this is when user submits an insert
def library_insert():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    query=""
    if request.method == 'POST':
		book_id = request.form['book_id']
		book_name = request.form['book_name']
		edition = request.form['edition']
		quantity = request.form['quantity']
		query = 'INSERT INTO library VALUES ({},{},{},{})'.format(book_id,book_name,edition,quantity)
		sql_insert_edit_delete(query)
	results = sql_query('SELECT * FROM library')
	return render_template('library.html', results=results)

@app.route('/library_delete',methods = ['POST', 'GET']) #this is when user clicks delete link
def library_delete():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'GET':
		book_id = request.args.get('book_id')
		query='DELETE FROM library WHERE book_id={}'.format(book_id)
		sql_insert_edit_delete(query)
	results = sql_query('SELECT * FROM library')
	return render_template('library.html', results=results)

@app.route('/library_edit1',methods = ['POST', 'GET']) #this is when user clicks edit link
def library_edit1():
    from functions.sqlquery import sql_query
    if request.method == 'GET':
		book_id = request.args.get('book_id')
		eresults = sql_query('SELECT * FROM library WHERE book_id={}'.format(book_id))
	results = sql_query("SELECT * FROM library")
	return render_template('library.html', eresults=eresults, results=results)

@app.route('/library_edit2',methods = ['POST', 'GET']) #this is when user submits an edit
def library_edit2():
    from functions.sqlquery import sql_insert_edit_delete, sql_query
    if request.method == 'POST':
		old_book_id = request.form['old_book_id']
		book_id = request.form['book_id']
		book_name = request.form['book_name']
		edition = request.form['edition']
		quantity = request.form['quantity']
		eresults = sql_query('SELECT * FROM library WHERE book_id={}'.format(book_id))
		query = 'UPDATE library set  book_id = {},book_name = {},edition = {},quantity = {} WHERE book_id = {}'.format(book_id,book_name,edition,quantity,old_book_id)
		sql_insert_edit_delete(query)
	results = sql_query('SELECT * FROM library')
	return render_template('library.html', results=results)

